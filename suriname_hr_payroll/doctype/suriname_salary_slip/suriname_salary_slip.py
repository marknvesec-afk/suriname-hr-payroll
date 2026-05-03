from frappe.model.document import Document
from suriname_hr_payroll.api.tax_calculator import calculate_tax
from suriname_hr_payroll.api.social_security import calculate_employee_ss, calculate_employer_ss
from suriname_hr_payroll.api.overtime_calculator import calculate_overtime
from frappe import _

class SurinameSalarySlip(Document):
    """Suriname Salary Slip Document"""

    def validate(self):
        """Validate salary slip"""
        self.calculate_salary()

    def calculate_salary(self):
        """Calculate salary components"""
        # Calculate total earnings
        self.total_earnings = (
            self.basic_salary + 
            (self.allowances or 0) + 
            (self.overtime_amount or 0) + 
            (self.bonus or 0)
        )

        self.gross_salary = self.total_earnings
        
        # Calculate deductions
        self.income_tax = calculate_tax(self.gross_salary)
        self.employee_social_security = calculate_employee_ss(self.gross_salary)
        
        self.total_deductions = (
            self.income_tax + 
            self.employee_social_security + 
            (self.other_deductions or 0)
        )

        # Calculate net pay
        self.net_pay = self.gross_salary - self.total_deductions
        
        # Employer contribution
        self.employer_social_security = calculate_employer_ss(self.gross_salary)
        
        # Total cost to company
        self.total_cost = self.gross_salary + self.employer_social_security
