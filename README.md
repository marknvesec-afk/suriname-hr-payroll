# Suriname HR/Payroll System - ERPNext Custom Module

A comprehensive, Suriname-compliant HR and Payroll management system built on ERPNext/Frappe framework. This system automates salary processing, tax calculations, and generates compliance-ready reports for Surinamese labor law.

## 📋 Features

### ✅ Core Payroll Management
- **Salary Structure**: Define salary components (basic, allowances, deductions)
- **Payroll Entry**: Process monthly payroll for multiple employees
- **Salary Slip**: Generate detailed, compliant payslips
- **Attendance Integration**: Auto-calculate overtime and leave deductions

### 💰 Suriname Tax & Compliance
- **Progressive Income Tax**: Automatic calculation (0%, 8%, 18%, 28%, 38% brackets)
- **Social Security Deductions**:
  - Employee: 2.5% (gradually increasing to 14% by 2065)
  - Employer: 14-16% contribution
- **FVO Declaration**: Monthly parental leave fund filing
- **Overtime Calculation**: 1.5x standard rate (2x for public holidays)
- **Minimum Wage Compliance**: SRD 60/hour validation

### 📊 Reports & Documentation
- Monthly Payroll Reports
- Salary Slip Generation (print-ready)
- Tax Declaration Reports
- FVO Monthly Declarations
- Leave & Attendance Reports
- Payroll Audit Trail (7-year retention)

### 👥 Employee Management
- Employee profiles with Suriname-specific fields
- Leave management (Annual, Sick, Maternity)
- Attendance tracking
- Contract management (Dutch language support)

### 🔐 Compliance Features
- Role-based permissions (HR Manager, Payroll Clerk, Employee)
- Document versioning & audit logs
- Workflow approvals (Draft → Submitted → Processed)
- 7-year record retention policy

---

## 🚀 Installation & Setup

### Prerequisites
- ERPNext v14.0 or higher
- Frappe v14.0 or higher
- Bench CLI installed
- Python 3.8+

### Step 1: Clone Repository
```bash
cd ~/frappe-bench/apps
git clone https://github.com/marknvesec-afk/suriname-hr-payroll.git
```

### Step 2: Install Dependencies
```bash
bench pip install -r suriname-hr-payroll/requirements.txt
```

### Step 3: Install App on Site
```bash
bench --site your-site install-app suriname-hr-payroll
```

### Step 4: Initialize Payroll Settings
Navigate to: **HR > Settings > Suriname Payroll Settings** and configure:
- Currency: SRD
- Minimum Wage: 60 SRD/hour
- Tax Brackets (pre-configured)
- Social Security Rates

---

## 📂 Project Structure

```
suraname-hr-payroll/
├── README.md
├── setup.py
├── requirements.txt
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── suriname_hr_payroll/
│   ├── __init__.py
│   ├── hooks.py
│   ├── doctype/
│   │   ├── suriname_payroll_settings/
│   │   ├── suriname_salary_structure/
│   │   ├── suriname_payroll_entry/
│   │   ├── suriname_salary_slip/
│   │   ├── suriname_fvo_declaration/
│   │   └── suriname_employee/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── tax_calculator.py
│   │   ├── social_security.py
│   │   ├── overtime_calculator.py
│   │   └── compliance.py
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── payroll_summary.py
│   │   ├── tax_declaration.py
│   │   ├── fvo_declaration.py
│   │   └── employee_payroll_register.py
│   └── utils/
│       ├── __init__.py
│       ├── validators.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_tax_calculator.py
│   ├── test_payroll_entry.py
│   ├── test_compliance.py
│   └── conftest.py
└── public/
    ├── css/
    │   └── payroll.css
    └── js/
        └── payroll_custom.js
```

---

## 🔧 Configuration

### Payroll Settings (Suriname Specific)
```
Company Currency: SRD
Minimum Wage: 60.00 per hour
Social Security Employee Rate: 2.5%
Social Security Employer Rate: 14-16%
Tax Brackets:
  - 0-2,646: 0%
  - 2,646-14,002: 8%
  - 14,003-21,919: 18%
  - 21,920-32,839: 28%
  - 32,840+: 38%
```

---

## 💡 Usage

### Processing Monthly Payroll
1. Go to **HR > Payroll > Suriname Payroll Entry**
2. Create new entry for the month
3. Select employees to process
4. System auto-calculates overtime, deductions, net pay
5. Review and approve
6. Generate salary slips
7. Generate FVO declaration

### Generating Payslips
1. Navigate to **HR > Payroll > Suriname Salary Slip**
2. View/print individual payslips
3. Export for employee distribution

---

## 🧪 Testing

```bash
# Run all tests
bench --site your-site frappe.bench frappe.test_runner --module suriname_hr_payroll

# Run specific test
bench --site your-site frappe.bench frappe.test_runner --module suriname_hr_payroll.tests.test_tax_calculator
```

---

## 📝 API Documentation

### Tax Calculator
```python
from suriname_hr_payroll.api.tax_calculator import calculate_tax

gross_salary = 25000  # SRD
tax = calculate_tax(gross_salary)
```

### Social Security
```python
from suriname_hr_payroll.api.social_security import calculate_employee_ss

employee_ss = calculate_employee_ss(25000)  # 625 SRD
```

---

## 📄 License

MIT License - See LICENSE file

---

**Built with ❤️ for Suriname businesses | ERPNext + Frappe**