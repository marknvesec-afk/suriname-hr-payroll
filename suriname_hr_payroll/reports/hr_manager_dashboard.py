from frappe import _

def execute(filters=None):
    """HR Manager Dashboard Report"""
    
    columns = [
        {
            "label": _("Metric"),
            "fieldname": "metric",
            "fieldtype": "Data",
            "width": 250,
        },
        {
            "label": _("Value"),
            "fieldname": "value",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100,
        }
    ]

    data = [
        {
            "metric": "Total Employees",
            "value": "0",
            "status": "Active"
        },
        {
            "metric": "Payroll Processed This Month",
            "value": "0",
            "status": "Pending"
        },
        {
            "metric": "Pending Leave Approvals",
            "value": "0",
            "status": "Action Required"
        },
        {
            "metric": "Compliance Issues",
            "value": "0",
            "status": "Clear"
        },
        {
            "metric": "Total Payroll Cost This Month",
            "value": "SRD 0.00",
            "status": "Reported"
        }
    ]

    return columns, data