from frappe.model.document import Document
from frappe import _
import frappe
from suriname_hr_payroll.api.overtime_calculator import calculate_overtime_from_attendance

class AttendanceIntegration(Document):
    """Attendance Integration for Overtime Calculation"""

    def validate(self):
        """Validate attendance integration"""
        if self.attendance_date_from > self.attendance_date_to:
            from frappe.exceptions import ValidationError
            raise ValidationError(_("From Date cannot be after To Date"))

    def on_submit(self):
        """Calculate overtime from attendance"""
        self.calculate_overtime()

    def calculate_overtime(self):
        """Calculate overtime for all employees"""
        for row in self.employees:
            # Fetch attendance records
            attendance_records = frappe.get_list(
                "Attendance",
                filters={
                    "employee": row.employee,
                    "attendance_date": [">=", self.attendance_date_from],
                    "attendance_date": ["<=", self.attendance_date_to],
                    "status": "Present"
                },
                fields=["working_hours"]
            )
            
            daily_hours = [record.working_hours or 0 for record in attendance_records]
            
            if daily_hours:
                # Get employee hourly rate
                employee = frappe.get_doc("Employee", row.employee)
                hourly_rate = employee.ctc / (40 * 52)  # Approximate hourly rate
                
                # Calculate overtime
                overtime_result = calculate_overtime_from_attendance(daily_hours, hourly_rate)
                
                row.overtime_hours = overtime_result["overtime_hours"]
                row.overtime_amount = overtime_result["overtime_amount"]
