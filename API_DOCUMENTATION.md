# Suriname HR/Payroll System - API Documentation

## Table of Contents
1. [Authentication](#authentication)
2. [API Endpoints](#api-endpoints)
3. [Tax Calculator API](#tax-calculator-api)
4. [Social Security API](#social-security-api)
5. [Overtime API](#overtime-api)
6. [Compliance API](#compliance-api)
7. [Error Handling](#error-handling)
8. [Code Examples](#code-examples)

---

## Authentication

All API calls require authentication headers:

```python
import frappe
from frappe.auth import HTTPBasicAuth

# Setup authentication
auth = HTTPBasicAuth('username', 'password')

# OR use API token
from frappe.client import get_value
from frappe import get_doc
```

---

## API Endpoints

### Payroll Entry

**Create Payroll Entry:**
```python
from frappe.client import insert

payroll_data = {
    "doctype": "Suriname Payroll Entry",
    "processing_month": "January",
    "processing_year": 2026,
    "company": "My Company Ltd",
    "posting_date": "2026-01-31"
}

payroll = insert(payroll_data)
print(f"Created: {payroll.name}")
```

**Get Payroll Entry:**
```python
from frappe import get_doc

payroll = get_doc("Suriname Payroll Entry", "SURINPAY-01-2026-00001")
print(f"Status: {payroll.status}")
print(f"Total Gross: {payroll.total_gross_salary}")
```

**Calculate Payroll:**
```python
from frappe.client import submit

payroll = get_doc("Suriname Payroll Entry", "SURINPAY-01-2026-00001")
payroll.calculate_payroll()
payroll.db_update()
print("Payroll calculated successfully")
```

**Submit Payroll:**
```python
payroll = get_doc("Suriname Payroll Entry", "SURINPAY-01-2026-00001")
payroll.submit()
print("Payroll submitted successfully")
```

---

## Tax Calculator API

### Calculate Income Tax

```python
from suriname_hr_payroll.api.tax_calculator import calculate_tax

# Basic usage
gross_salary = 25000  # SRD
tax = calculate_tax(gross_salary)
print(f"Tax for SRD {gross_salary}: SRD {tax}")
# Output: Tax for SRD 25000: SRD 3195.00
```

### Get Tax Bracket

```python
from suriname_hr_payroll.api.tax_calculator import get_tax_bracket

salary = 20000
bracket = get_tax_bracket(salary)
print(f"Bracket Rate: {bracket['rate']}%")
print(f"Range: SRD {bracket['min']} - SRD {bracket['max']}")
# Output:
# Bracket Rate: 18%
# Range: SRD 14003 - SRD 21919
```

### Get Effective Tax Rate

```python
from suriname_hr_payroll.api.tax_calculator import get_effective_tax_rate

salary = 30000
effective_rate = get_effective_tax_rate(salary)
print(f"Effective tax rate: {effective_rate}%")
# Output: Effective tax rate: 12.75%
```

### Tax Brackets Reference

| Range (SRD) | Tax Rate |
|-------------|----------|
| 0 - 2,646 | 0% |
| 2,646 - 14,002 | 8% |
| 14,003 - 21,919 | 18% |
| 21,920 - 32,839 | 28% |
| 32,840+ | 38% |

---

## Social Security API

### Calculate Employee Social Security

```python
from suriname_hr_payroll.api.social_security import calculate_employee_ss

gross_salary = 25000  # SRD
emp_ss = calculate_employee_ss(gross_salary)
print(f"Employee SS (2.5%): SRD {emp_ss}")
# Output: Employee SS (2.5%): SRD 625.00

# Custom rate
emp_ss_custom = calculate_employee_ss(gross_salary, rate=0.03)
print(f"Employee SS (3%): SRD {emp_ss_custom}")
# Output: Employee SS (3%): SRD 750.00
```

### Calculate Employer Social Security

```python
from suriname_hr_payroll.api.social_security import calculate_employer_ss

gross_salary = 25000  # SRD
emp_contrib = calculate_employer_ss(gross_salary)  # Default 14%
print(f"Employer SS (14%): SRD {emp_contrib}")
# Output: Employer SS (14%): SRD 3500.00

# Custom rate (16%)
emp_contrib_high = calculate_employer_ss(gross_salary, rate=0.16)
print(f"Employer SS (16%): SRD {emp_contrib_high}")
# Output: Employer SS (16%): SRD 4000.00
```

### Calculate Total Social Security Cost

```python
from suriname_hr_payroll.api.social_security import calculate_total_ss_cost

gross_salary = 25000
ss_cost = calculate_total_ss_cost(gross_salary)
print(f"Employee SS: SRD {ss_cost['employee_ss']}")
print(f"Employer SS: SRD {ss_cost['employer_ss']}")
print(f"Total SS: SRD {ss_cost['total_ss']}")
# Output:
# Employee SS: SRD 625.00
# Employer SS: SRD 3500.00
# Total SS: SRD 4125.00
```

---

## Overtime API

### Calculate Overtime Pay

```python
from suriname_hr_payroll.api.overtime_calculator import calculate_overtime

# Standard overtime (1.5x rate)
hourly_rate = 60  # SRD
overtime_hours = 5
overtime_pay = calculate_overtime(hourly_rate, overtime_hours)
print(f"Overtime pay (1.5x): SRD {overtime_pay}")
# Output: Overtime pay (1.5x): SRD 450.00

# Holiday overtime (2x rate)
holiday_pay = calculate_overtime(hourly_rate, overtime_hours, multiplier=2.0)
print(f"Holiday pay (2x): SRD {holiday_pay}")
# Output: Holiday pay (2x): SRD 600.00
```

### Calculate Overtime from Attendance

```python
from suriname_hr_payroll.api.overtime_calculator import calculate_overtime_from_attendance

# Daily hours worked
daily_hours = [8, 8, 8, 10, 10, 8, 8]  # Mon-Sun
hourly_rate = 60
result = calculate_overtime_from_attendance(daily_hours, hourly_rate)
print(f"Overtime hours: {result['overtime_hours']}")
print(f"Overtime amount: SRD {result['overtime_amount']}")
# Output:
# Overtime hours: 4.0
# Overtime amount: SRD 360.00
```

### Calculate Weekly Overtime

```python
from suriname_hr_payroll.api.overtime_calculator import calculate_weekly_overtime

weekly_hours = [8, 8, 8, 8, 8, 0, 0]  # Mon-Fri
hourly_rate = 60
result = calculate_weekly_overtime(weekly_hours, hourly_rate, max_weekly_hours=40)
print(f"Total hours: {result['total_hours']}")
print(f"Overtime hours: {result['overtime_hours']}")
print(f"Overtime amount: SRD {result['overtime_amount']}")
# Output:
# Total hours: 40
# Overtime hours: 0
# Overtime amount: SRD 0.00
```

---

## Compliance API

### Validate Minimum Wage

```python
from suriname_hr_payroll.api.compliance import validate_minimum_wage

hourly_rate = 60  # SRD
result = validate_minimum_wage(hourly_rate)
print(f"Minimum wage compliant: {result}")
# Output: Minimum wage compliant: True

low_rate = 50
result = validate_minimum_wage(low_rate)
print(f"Minimum wage compliant: {result}")
# Output: Minimum wage compliant: False
```

### Get Notice Period

```python
from suriname_hr_payroll.api.compliance import get_notice_period_days

# Less than 1 year
notice_days = get_notice_period_days(0.5)
print(f"Notice period: {notice_days} weeks")
# Output: Notice period: 1 weeks

# 3 years service
notice_days = get_notice_period_days(3)
print(f"Notice period: {notice_days} weeks")
# Output: Notice period: 4 weeks (1 month)

# 15 years service
notice_days = get_notice_period_days(15)
print(f"Notice period: {notice_days} weeks")
# Output: Notice period: 12 weeks (3 months)
```

### Validate Leave Entitlement

```python
from suriname_hr_payroll.api.compliance import validate_leave_entitlement

# Full year of service
result = validate_leave_entitlement(tenure_months=12, leave_days_used=10)
print(f"Entitled: {result['entitled_days']} days")
print(f"Used: {result['used_days']} days")
print(f"Remaining: {result['remaining_days']} days")
print(f"Compliant: {result['is_compliant']}")
# Output:
# Entitled: 12 days
# Used: 10 days
# Remaining: 2 days
# Compliant: True

# Partial year
result = validate_leave_entitlement(tenure_months=6, leave_days_used=5)
print(f"Entitled (6 months): {result['entitled_days']} days")
# Output: Entitled (6 months): 6.0 days
```

---

## Error Handling

### Common Errors and Solutions

```python
from frappe.exceptions import ValidationError, PermissionError

try:
    # Try to process payroll
    payroll = get_doc("Suriname Payroll Entry", "SURINPAY-01-2026-00001")
    payroll.calculate_payroll()
    payroll.submit()
except ValidationError as e:
    print(f"Validation Error: {e}")
    # Handle: Missing required fields, invalid data
except PermissionError as e:
    print(f"Permission Error: {e}")
    # Handle: User doesn't have permission
except Exception as e:
    print(f"Unexpected Error: {e}")
    # Handle: Other errors
```

### Error Responses

```json
{
  "error": {
    "type": "ValidationError",
    "message": "Processing Month and Year are required"
  }
}
```

---

## Code Examples

### Complete Payroll Processing Workflow

```python
from frappe import get_doc
from frappe.client import insert, submit
from suriname_hr_payroll.api.tax_calculator import calculate_tax
from suriname_hr_payroll.api.social_security import calculate_employee_ss, calculate_employer_ss

# Step 1: Create Payroll Entry
payroll_data = {
    "doctype": "Suriname Payroll Entry",
    "processing_month": "January",
    "processing_year": 2026,
    "company": "My Company Ltd"
}

payroll = insert(payroll_data)
print(f"Created Payroll Entry: {payroll.name}")

# Step 2: Load Employees (simulated)
employee_salaries = [
    {"employee": "EMP001", "gross_salary": 25000},
    {"employee": "EMP002", "gross_salary": 20000},
    {"employee": "EMP003", "gross_salary": 15000},
]

# Step 3: Calculate for each employee
for emp in employee_salaries:
    gross = emp["gross_salary"]
    tax = calculate_tax(gross)
    emp_ss = calculate_employee_ss(gross)
    emp_contrib = calculate_employer_ss(gross)
    net_pay = gross - tax - emp_ss
    
    print(f"\nEmployee: {emp['employee']}")
    print(f"Gross: SRD {gross:.2f}")
    print(f"Tax: SRD {tax:.2f}")
    print(f"SS (Emp): SRD {emp_ss:.2f}")
    print(f"SS (Emp Contrib): SRD {emp_contrib:.2f}")
    print(f"Net: SRD {net_pay:.2f}")

# Step 4: Submit
payroll = get_doc("Suriname Payroll Entry", payroll.name)
payroll.submit()
print(f"\nPayroll Submitted: {payroll.name}")
```

### Batch Salary Slip Generation

```python
from frappe import get_list, get_doc

# Get all salary slips for January 2026
slips = get_list(
    "Suriname Salary Slip",
    filters={
        "salary_month": "January",
        "salary_year": 2026
    },
    fields=["name", "employee", "net_pay"]
)

# Process each slip
total_net_pay = 0
for slip in slips:
    slip_doc = get_doc("Suriname Salary Slip", slip.name)
    total_net_pay += slip_doc.net_pay
    print(f"Slip: {slip.name}, Employee: {slip.employee}, Net: SRD {slip_doc.net_pay}")

print(f"\nTotal Net Pay for January: SRD {total_net_pay}")
```

### Tax Declaration Report

```python
from frappe import get_list
from suriname_hr_payroll.api.tax_calculator import get_effective_tax_rate

# Get all salary slips for the month
slips = get_list(
    "Suriname Salary Slip",
    filters={
        "salary_month": "January",
        "salary_year": 2026
    },
    fields=["name", "employee", "gross_salary", "income_tax"]
)

print("TAX DECLARATION REPORT - January 2026")
print("="*60)

total_gross = 0
total_tax = 0

for slip in slips:
    effective_rate = get_effective_tax_rate(slip.gross_salary)
    total_gross += slip.gross_salary
    total_tax += slip.income_tax
    
    print(f"Employee: {slip.employee}")
    print(f"  Gross: SRD {slip.gross_salary:.2f}")
    print(f"  Tax: SRD {slip.income_tax:.2f}")
    print(f"  Rate: {effective_rate}%")
    print()

print("="*60)
print(f"Total Gross Salary: SRD {total_gross:.2f}")
print(f"Total Tax: SRD {total_tax:.2f}")
print(f"Average Tax Rate: {(total_tax/total_gross)*100:.2f}%")
```

---

## Function Reference

### Tax Calculator Functions

| Function | Parameters | Returns | Example |
|----------|-----------|---------|----------|
| `calculate_tax()` | gross_salary (float) | float (tax amount) | `calculate_tax(25000)` → 3195.00 |
| `get_tax_bracket()` | gross_salary (float) | dict (bracket info) | `get_tax_bracket(20000)` → {min: 14003, max: 21919, rate: 0.18} |
| `get_effective_tax_rate()` | gross_salary (float) | float (percentage) | `get_effective_tax_rate(25000)` → 12.78 |

### Social Security Functions

| Function | Parameters | Returns | Example |
|----------|-----------|---------|----------|
| `calculate_employee_ss()` | gross_salary, rate=None | float (SS amount) | `calculate_employee_ss(25000)` → 625.00 |
| `calculate_employer_ss()` | gross_salary, rate=None | float (SS amount) | `calculate_employer_ss(25000)` → 3500.00 |
| `calculate_total_ss_cost()` | gross_salary, employer_rate | dict (costs) | `calculate_total_ss_cost(25000)` → {employee_ss: 625, employer_ss: 3500, total_ss: 4125} |

### Overtime Functions

| Function | Parameters | Returns | Example |
|----------|-----------|---------|----------|
| `calculate_overtime()` | hourly_rate, hours, multiplier | float (amount) | `calculate_overtime(60, 5)` → 450.00 |
| `calculate_overtime_from_attendance()` | daily_hours, hourly_rate, max_daily | dict (hours, amount) | `calculate_overtime_from_attendance([8,8,8,10,10])` |
| `calculate_weekly_overtime()` | weekly_hours, hourly_rate, max_weekly | dict (details) | `calculate_weekly_overtime([8]*5, 60)` |

---

## Support

For API support:
- 📧 Email: support@company.com
- 🐙 GitHub: https://github.com/marknvesec-afk/suriname-hr-payroll/issues
- 📖 Docs: https://github.com/marknvesec-afk/suriname-hr-payroll

---

**API Documentation v1.0.0 | Last Updated: May 3, 2026**