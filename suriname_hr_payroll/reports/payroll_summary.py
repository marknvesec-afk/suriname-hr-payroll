"""
Payroll Summary Report
Monthly payroll overview
"""

from frappe import _


def execute(filters=None):
    """Execute payroll summary report"""
    columns = [
        {
            "label": _("Employee"),
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 150,
        },
        {"label": _("Gross Salary"), "fieldname": "gross_salary", "fieldtype": "Currency", "width": 120},
        {"label": _("Income Tax"), "fieldname": "income_tax", "fieldtype": "Currency", "width": 120},
        {"label": _("Social Security"), "fieldname": "social_security", "fieldtype": "Currency", "width": 120},
        {"label": _("Net Pay"), "fieldname": "net_pay", "fieldtype": "Currency", "width": 120},
    ]

    data = []

    return columns, data