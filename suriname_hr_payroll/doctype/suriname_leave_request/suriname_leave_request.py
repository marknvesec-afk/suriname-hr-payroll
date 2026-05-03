from frappe.model.document import Document
from frappe import _
import frappe
from datetime import datetime

class SurinameLeaveRequest(Document):
    """Suriname Leave Request Document"""

    def validate(self):
        """Validate leave request"""
        if self.from_date >= self.to_date:
            from frappe.exceptions import ValidationError
            raise ValidationError(_("From Date must be before To Date"))
        
        # Calculate number of days
        delta = self.to_date - self.from_date
        self.number_of_days = delta.days + 1
        
        # Check leave balance
        self.check_leave_balance()

    def check_leave_balance(self):
        """Check if employee has sufficient leave balance"""
        # Get employee
        employee = frappe.get_doc("Employee", self.employee)
        
        # Calculate leave balance (simplified)
        self.opening_balance = 12  # Default annual leave
        self.days_used = self.number_of_days
        self.closing_balance = self.opening_balance - self.days_used
        
        if self.closing_balance < 0 and self.leave_type == "Annual":
            from frappe.exceptions import ValidationError
            raise ValidationError(_("Insufficient leave balance. Available: {0}, Requested: {1}").format(
                self.opening_balance, self.number_of_days
            ))

    def on_submit(self):
        """On submit of leave request"""
        self.status = "Approved"
        self.approval_status = "Approved"
