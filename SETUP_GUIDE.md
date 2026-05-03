# Suriname HR/Payroll System - Complete Setup Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Configuration Guide](#configuration-guide)
4. [Data Setup](#data-setup)
5. [Processing First Payroll](#processing-first-payroll)
6. [Reports & Compliance](#reports--compliance)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements
- **ERPNext**: v14.0 or higher
- **Frappe**: v14.0 or higher
- **Python**: 3.8 or higher
- **Node.js**: 14.0 or higher
- **MariaDB/MySQL**: 5.7 or higher
- **Ubuntu/Debian**: 18.04 LTS or higher

### Required Modules
- HR module (ERPNext)
- Payroll module (ERPNext)
- Attendance module (ERPNext)
- Leave Management (ERPNext)

---

## Installation Steps

### Step 1: Clone the Repository

```bash
# Navigate to bench apps directory
cd ~/frappe-bench/apps

# Clone the repository
git clone https://github.com/marknvesec-afk/suriname-hr-payroll.git

# Verify cloning
ls -la suriname-hr-payroll/
```

**Expected Output:**
```
drwxr-xr-x  suriname_hr_payroll/
drwxr-xr-x  tests/
drwxr-xr-x  public/
-rw-r--r--  README.md
-rw-r--r--  setup.py
-rw-r--r--  requirements.txt
```

### Step 2: Install Dependencies

```bash
# Go to bench directory
cd ~/frappe-bench

# Install Python dependencies
bench pip install -r apps/suriname-hr-payroll/requirements.txt

# Verify installation
bench pip show frappe
```

### Step 3: Install App on Site

```bash
# Install the app
bench --site your-site-name install-app suriname-hr-payroll

# Expected output:
# Installing suriname-hr-payroll...
# Migrating...
# Done
```

**Note:** Replace `your-site-name` with your actual site name (e.g., `erpnext.local`)

### Step 4: Verify Installation

```bash
# Access ERPNext
bench browse your-site-name

# Navigate to: Awesome Bar > Suriname Payroll Settings
# You should see the Suriname Payroll menu
```

---

## Configuration Guide

### Step 1: Create Suriname Payroll Settings

1. **Navigate to:** HR → Settings → Suriname Payroll Settings
2. **Click:** New
3. **Fill in the following:**

| Field | Value | Example |
|-------|-------|----------|
| Company | Link to your company | My Company Ltd |
| Currency | SRD | SRD |
| Minimum Wage (per hour) | 60.00 | 60.00 |
| Employee SS Rate (%) | 2.5 | 2.5 |
| Employer SS Rate Min (%) | 14.0 | 14.0 |
| Employer SS Rate Max (%) | 16.0 | 16.0 |
| Tax Bracket 1 Min | 0 | 0 |
| Tax Bracket 1 Max | 2646 | 2646 |
| Tax Bracket 1 Rate (%) | 0 | 0 |
| Tax Bracket 2 Min | 2646 | 2646 |
| Tax Bracket 2 Max | 14002 | 14002 |
| Tax Bracket 2 Rate (%) | 8 | 8 |
| Tax Bracket 3 Min | 14003 | 14003 |
| Tax Bracket 3 Max | 21919 | 21919 |
| Tax Bracket 3 Rate (%) | 18 | 18 |
| Tax Bracket 4 Min | 21920 | 21920 |
| Tax Bracket 4 Max | 32839 | 32839 |
| Tax Bracket 4 Rate (%) | 28 | 28 |
| Tax Bracket 5 Min | 32840 | 32840 |
| Tax Bracket 5 Max | 999999 | 999999 |
| Tax Bracket 5 Rate (%) | 38 | 38 |
| Record Retention Years | 7 | 7 |

4. **Save & Submit**

### Step 2: Create Salary Structures

1. **Navigate to:** HR → Settings → Salary Structure
2. **Click:** New
3. **Configure for each position:**

```
Salary Structure Name: Manager - 2026
Company: My Company Ltd
Payroll Frequency: Monthly

Salary Components:
├── Earnings
│   ├── Basic Salary - 20000 SRD
│   ├── Housing Allowance - 3000 SRD
│   ├── Transport Allowance - 1500 SRD
│   ├── Meal Allowance - 500 SRD
│   └── Performance Bonus - Variable
├── Deductions
│   ├── Income Tax - Calculated
│   ├── Employee Social Security - 2.5%
│   └── Other Deductions - As applicable
```

4. **Save & Submit**

---

## Data Setup

### Step 1: Import Employees

#### Method 1: Bulk Import via CSV

1. **Create CSV file** with columns:
```csv
first_name,last_name,email,company,designation,department,date_of_joining,ctc,minimum_wage_compliant
John,Doe,john@example.com,My Company Ltd,Manager,Operations,2025-01-01,180000,1
Jane,Smith,jane@example.com,My Company Ltd,Supervisor,Operations,2025-02-01,120000,1
```

2. **Navigate to:** HR → Employee → Menu (⋮) → Import
3. **Upload CSV file**
4. **Verify data** and submit

#### Method 2: Manual Entry

1. **Navigate to:** HR → Employee → New
2. **Fill employee details:**
   - First Name
   - Last Name
   - Email
   - Company
   - Designation
   - Department
   - Date of Joining
   - CTC (Cost to Company)

3. **Save & Submit**

### Step 2: Create Designations

```
1. Manager
2. Supervisor
3. Operator
4. Admin
5. Support Staff
```

### Step 3: Create Departments

```
1. Operations
2. Finance
3. HR
4. IT
5. Sales
6. Marketing
```

### Step 4: Link Attendance System

1. **Verify Attendance** is already recorded in ERPNext
2. **Check attendance records:**
   - Navigate to: HR → Attendance
   - Verify employees & dates are correct

---

## Processing First Payroll

### Step 1: Create Payroll Entry

1. **Navigate to:** HR → Payroll → Suriname Payroll Entry
2. **Click:** New
3. **Fill in details:**
   - Processing Month: (e.g., January)
   - Processing Year: 2026
   - Company: My Company Ltd
   - Posting Date: Today

### Step 2: Load Employees

1. **Click:** Load Employees button
2. **System will:**
   - Fetch all active employees
   - Add them to the table
   - Load from salary structure

### Step 3: Calculate Payroll

1. **Click:** Calculate Payroll button
2. **System will:**
   - Calculate gross salary
   - Apply tax (progressive)
   - Deduct social security (2.5%)
   - Calculate net pay
   - Update all summary fields

### Step 4: Review Summary

Check the following totals:
- Total Employees
- Total Gross Salary (SRD)
- Total Income Tax (SRD)
- Total Employee SS (SRD)
- Total Employer SS (SRD)
- Total Net Pay (SRD)

### Step 5: Submit Payroll Entry

1. **Click:** Submit button
2. **Confirmation message** will appear
3. **System will:**
   - Lock the document
   - Generate salary slips automatically
   - Create journal entries (optional)

### Step 6: Generate Salary Slips

1. **Click:** Generate Salary Slips button
2. **Select:** All employees (or specific employees)
3. **Click:** Generate
4. **System will:**
   - Create individual salary slips
   - Calculate detailed breakdowns
   - Prepare for printing/emailing

---

## Reports & Compliance

### Monthly Tax Declaration

1. **Navigate to:** Reports → Tax Declaration
2. **Select:** Month and Year
3. **Download:** PDF or Excel
4. **File with:** Tax Authority (FVO)

### FVO Declaration

1. **Navigate to:** HR → Payroll → FVO Declaration
2. **Create:** New FVO Declaration
3. **Load:** Employees with dependents
4. **Submit:** To government within 5 days

### HR Analytics Dashboard

1. **Navigate to:** HR → Reports → HR Manager Dashboard
2. **View:**
   - Total employees
   - Payroll cost trends
   - Compliance status
   - Leave analytics

---

## Troubleshooting

### Issue: "Module not found" error

**Solution:**
```bash
bench clear-cache
bench --site your-site migrate
bench --site your-site install-app suriname-hr-payroll
```

### Issue: Tax calculations not showing

**Solution:**
1. Verify Suriname Payroll Settings are configured
2. Check tax brackets are set correctly
3. Ensure employee has salary structure

### Issue: Employees not loading in payroll entry

**Solution:**
1. Verify employees are in "Active" status
2. Check employees have valid designation
3. Ensure salary structure is assigned

### Issue: Can't submit payroll entry

**Solution:**
1. Check for mandatory fields
2. Verify all amounts are calculated
3. Check for duplicate entries

---

## Quick Reference

### Keyboard Shortcuts
- **Ctrl+S**: Save
- **Ctrl+Enter**: Submit
- **Ctrl+Q**: Quick Entry

### Common Workflows

**Monthly Payroll Processing:**
```
1. Suriname Payroll Entry → New
2. Select Month & Year
3. Load Employees
4. Calculate Payroll
5. Review Summary
6. Submit
7. Generate Salary Slips
8. Generate Reports
```

**Leave Processing:**
```
1. Suriname Leave Request → New
2. Select Employee & Leave Type
3. Enter Dates
4. Submit (Auto-approved)
5. View on Employee Dashboard
```

---

## Support & Documentation

- **GitHub:** https://github.com/marknvesec-afk/suriname-hr-payroll
- **Documentation:** See README.md
- **Issues:** Report on GitHub Issues
- **Contact:** For support, open an issue

---

**Setup Complete! You're ready to process payroll.** 🎉