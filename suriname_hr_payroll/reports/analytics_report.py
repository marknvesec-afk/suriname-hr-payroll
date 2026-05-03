from frappe import _
import frappe
from datetime import date

def execute(filters=None):
    """Analytics Report for HR Performance"""
    
    columns = [
        {
            "label": _("Month"),
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("Total Gross Salary (SRD)"),
            "fieldname": "total_gross",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": _("Total Tax (SRD)"),
            "fieldname": "total_tax",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": _("Total Net Pay (SRD)"),
            "fieldname": "total_net",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": _("Avg Effective Tax Rate (%)"),
            "fieldname": "avg_tax_rate",
            "fieldtype": "Percent",
            "width": 150,
        }
    ]

    data = []

    return columns, data