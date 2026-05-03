app_name = "suriname_hr_payroll"
app_title = "Suriname HR/Payroll"
app_publisher = "Mark Nvesec"
app_description = "Suriname-compliant HR and Payroll management system"
app_icon = "fa fa-briefcase"
app_color = "#FF6B35"
app_email = "marknvesec@example.com"
app_license = "MIT"

# Include Frappe modules
modules = [
    {
        "label": "HR Payroll",
        "items": [
            "Suriname Payroll Settings",
            "Suriname Salary Structure",
            "Suriname Payroll Entry",
            "Suriname Salary Slip",
            "Suriname FVO Declaration",
        ],
    }
]

# Fixtures
fixtures = []

# Permissions
permissions = [
    {
        "role": "HR Manager",
        "perms": [
            {"doctype": "Suriname Payroll Settings", "perm": ["read", "write", "submit", "admin"]},
            {"doctype": "Suriname Salary Structure", "perm": ["read", "write", "create", "delete"]},
            {"doctype": "Suriname Payroll Entry", "perm": ["read", "write", "create", "submit"]},
            {"doctype": "Suriname Salary Slip", "perm": ["read", "write", "print"]},
            {"doctype": "Suriname FVO Declaration", "perm": ["read", "write"]},
        ],
    },
    {
        "role": "Employee",
        "perms": [
            {"doctype": "Suriname Salary Slip", "perm": ["read"]},
        ],
    },
]

# API Methods
api_methods = {}

# Document Hooks
doc_events = {}

# Celery Beat Schedule
celery_beat_schedule = {}

# Scheduler Jobs
scheduler_jobs = [
    {
        "method": "suriname_hr_payroll.utils.schedulers.monthly_payroll_reminder",
        "interval": ["monthly"],
    }
]

# Migrate
migrate = []

# Website routes
website_route_rules = []

# Desk Sidebar
desk_sidebar = [
    {
        "module": "HR",
        "label": "Payroll",
        "items": [
            "Suriname Payroll Settings",
            "Suriname Salary Structure",
            "Suriname Payroll Entry",
            "Suriname Salary Slip",
            "Suriname FVO Declaration",
        ],
    }
]