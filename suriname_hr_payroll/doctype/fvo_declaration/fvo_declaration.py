from frappe.model.document import Document
from frappe import _
import frappe

class FVODeclaration(Document):
    """FVO (Parental Leave Fund) Declaration Document"""

    def validate(self):
        """Validate FVO declaration"""
        if not self.employees:
            from frappe.exceptions import ValidationError
            raise ValidationError(_("At least one employee with dependents is required"))

    def on_submit(self):
        """Calculate FVO totals on submit"""
        self.calculate_fvo_totals()
        self.status = "Submitted"
        self.db_update()

    def calculate_fvo_totals(self):
        """Calculate total FVO amount and employee count"""
        total_amount = 0
        employee_count = 0
        
        for row in self.employees:
            if row.has_dependents:
                total_amount += row.fvo_amount or 0
                employee_count += 1
        
        self.total_employees_with_dependents = employee_count
        self.total_fvo_amount = total_amount
