from frappe.model.document import Document
from suriname_hr_payroll.api.tax_calculator import calculate_tax
from suriname_hr_payroll.api.social_security import calculate_employee_ss, calculate_employer_ss
from frappe import _

class SurinamepayrollEntry(Document):
    """Suriname Payroll Entry Document"""

    def validate(self):
        """Validate payroll entry"""
        if not self.processing_month or not self.processing_year:
            from frappe.exceptions import ValidationError
            raise ValidationError(_("Processing Month and Year are required"))

    def on_submit(self):
        """Calculate payroll on submit"""
        self.calculate_payroll()
        self.status = "Completed"
        self.db_update()

    def calculate_payroll(self):
        """Calculate payroll for all employees"""
        total_gross = 0
        total_tax = 0
        total_employee_ss = 0
        total_employer_ss = 0

        for row in self.employees:
            gross_salary = row.gross_salary
            
            # Calculate deductions
            income_tax = calculate_tax(gross_salary)
            emp_ss = calculate_employee_ss(gross_salary)
            emp_contribution = calculate_employer_ss(gross_salary)
            
            # Calculate net pay
            net_pay = gross_salary - income_tax - emp_ss
            
            # Update row
            row.income_tax = income_tax
            row.employee_social_security = emp_ss
            row.employer_contribution = emp_contribution
            row.net_pay = net_pay
            
            # Add to totals
            total_gross += gross_salary
            total_tax += income_tax
            total_employee_ss += emp_ss
            total_employer_ss += emp_contribution

        # Update summary
        self.total_employees = len(self.employees)
        self.total_gross_salary = total_gross
        self.total_income_tax = total_tax
        self.total_social_security = total_employee_ss
        self.total_employer_contribution = total_employer_ss
        self.total_net_pay = total_gross - total_tax - total_employee_ss
