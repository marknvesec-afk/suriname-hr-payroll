from frappe.model.document import Document
from frappe import _
import frappe
from datetime import datetime, date

class EmployeeDashboard(Document):
    """Employee Self-Service Dashboard"""

    def load(self):
        """Load employee dashboard data"""
        super().load()
        self.populate_payroll_data()
        self.populate_leave_data()

    def populate_payroll_data(self):
        """Populate current payroll information"""
        today = date.today()
        self.current_month = today.strftime("%B")
        self.current_year = today.year
        
        # Get latest salary slip
        latest_slip = frappe.get_list(
            "Suriname Salary Slip",
            filters={"employee": self.employee},
            fields=["gross_salary", "income_tax", "employee_social_security", "net_pay"],
            order_by="posting_date desc",
            limit_page_length=1
        )
        
        if latest_slip:
            slip = latest_slip[0]
            self.gross_salary = slip.get("gross_salary")
            self.income_tax = slip.get("income_tax")
            self.social_security = slip.get("employee_social_security")
            self.net_pay = slip.get("net_pay")

    def populate_leave_data(self):
        """Populate leave balance information"""
        # Calculate leave balances
        self.annual_leave_balance = 12  # Default
        self.sick_leave_balance = 10    # Default
        self.maternity_leave_balance = 84  # 12 weeks
        
        # Get leaves taken this year
        year_start = date(date.today().year, 1, 1)
        leaves_taken = frappe.get_list(
            "Suriname Leave Request",
            filters={
                "employee": self.employee,
                "status": "Approved",
                "from_date": [">=", year_start]
            },
            fields=["number_of_days"]
        )
        
        self.leaves_taken_this_year = sum([l.get("number_of_days", 0) for l in leaves_taken])
        
        # Get pending leaves
        pending_leaves = frappe.get_list(
            "Suriname Leave Request",
            filters={"employee": self.employee, "status": "Pending"},
            fields=["number_of_days"]
        )
        
        self.leaves_pending_approval = len(pending_leaves)
