"""
FVO Declaration Report
Parental leave fund monthly declarations
"""

from frappe import _


def execute(filters=None):
    """Execute FVO declaration report"""
    columns = [
        {"label": _("Employee"), "fieldname": "employee", "fieldtype": "Link", "options": "Employee"},
        {"label": _("Has Dependents"), "fieldname": "has_dependents", "fieldtype": "Check"},
        {"label": _("FVO Amount"), "fieldname": "fvo_amount", "fieldtype": "Currency"},
        {"label": _("Declaration Status"), "fieldname": "declaration_status", "fieldtype": "Data"},
    ]

    data = []

    return columns, data