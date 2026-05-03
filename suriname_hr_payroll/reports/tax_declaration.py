"""
Tax Declaration Report
Monthly tax summary for compliance
"""

from frappe import _


def execute(filters=None):
    """Execute tax declaration report"""
    columns = [
        {"label": _("Employee"), "fieldname": "employee", "fieldtype": "Link", "options": "Employee"},
        {"label": _("Gross Salary"), "fieldname": "gross_salary", "fieldtype": "Currency"},
        {"label": _("Taxable Income"), "fieldname": "taxable_income", "fieldtype": "Currency"},
        {"label": _("Tax Rate"), "fieldname": "tax_rate", "fieldtype": "Percent"},
        {"label": _("Income Tax"), "fieldname": "income_tax", "fieldtype": "Currency"},
    ]

    data = []

    return columns, data