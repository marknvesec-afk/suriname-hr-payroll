# Suriname HR/Payroll System - User Manual

## Table of Contents
1. [HR Manager Guide](#hr-manager-guide)
2. [Payroll Officer Guide](#payroll-officer-guide)
3. [Employee Guide](#employee-guide)
4. [FAQ](#faq)
5. [Best Practices](#best-practices)

---

## HR Manager Guide

### 1. Viewing HR Dashboard

**Path:** HR → Reports → HR Manager Dashboard

**What You See:**
- Total active employees
- Pending leave approvals
- Pending payroll tasks
- Compliance issues (if any)
- Monthly payroll costs

**Actions Available:**
- ✅ Approve/reject leave requests
- ✅ View payroll summary
- ✅ Generate compliance reports
- ✅ Monitor tax filings

### 2. Managing Leave Approvals

**Step 1: Access Leave Requests**
- Navigate to: HR → Leave Management → Suriname Leave Request
- Filter by: Status = "Pending Manager"

**Step 2: Review Leave Request**
- Click on the leave request
- Verify employee details
- Check leave balance
- Review dates and leave type

**Step 3: Approve or Reject**
- Click: Approve button (to approve)
- Click: Reject button (to reject with reason)
- Leave request updates automatically
- Email notification sent to employee

**Leave Types:**
- 🏖️ **Annual Leave** (12-15 days/year)
- 🤒 **Sick Leave** (As needed)
- 🍼 **Maternity Leave** (12 weeks paid)
- 🎓 **Special Leave** (As defined)

### 3. Monitoring Compliance

**Monthly Compliance Checklist:**
```
☐ All employees in system
☐ Salary structures assigned
☐ Attendance recorded
☐ Payroll processed
☐ Salary slips generated
☐ Taxes paid
☐ Social security filed
☐ FVO declaration submitted
```

---

## Payroll Officer Guide

### 1. Processing Monthly Payroll

**Step 1: Create Payroll Entry**

```
Path: HR → Payroll → Suriname Payroll Entry → New

Fill in:
- Processing Month: [Select month]
- Processing Year: 2026
- Company: My Company Ltd
- Posting Date: Today
```

**Step 2: Load Employees**

```
Click: "Load Employees" button

System will:
✓ Fetch all active employees
✓ Populate basic salary
✓ Link salary structures
✓ Show in table
```

**Step 3: Calculate Payroll**

```
Click: "Calculate Payroll" button

System calculates:
✓ Gross salary (Basic + Allowances + Overtime)
✓ Income Tax (Progressive brackets)
✓ Social Security (2.5% employee deduction)
✓ Net Pay (Gross - Tax - SS)
✓ Employer SS (14-16%)
```

**Step 4: Review Summary**

```
Verify totals:
- Total Employees: ___
- Total Gross Salary (SRD): ___
- Total Income Tax (SRD): ___
- Total Employee SS (SRD): ___
- Total Net Pay (SRD): ___
```

**Step 5: Submit Payroll**

```
Click: "Submit" button

Confirmation:
✓ Payroll locked
✓ Salary slips generated
✓ Journal entries created
✓ Email notifications sent
```

### 2. Generating Salary Slips

**Automatic Generation:**
- Salary slips auto-generated on payroll submission
- One slip per employee
- Includes all earnings & deductions

**Manual Generation:**
```
Path: HR → Payroll → Suriname Payroll Entry
Click: "Generate Salary Slips" button
Select: Employees
Click: Generate
```

**Print Salary Slip:**
```
Path: HR → Payroll → Suriname Salary Slip
Select: Employee's slip
Click: Print → Download PDF
```

### 3. Tax & Compliance Reporting

**Tax Declaration Report:**

```
Path: Reports → Tax Declaration

Select:
- Month
- Year
- Company

Download:
✓ PDF (for printing)
✓ Excel (for analysis)
✓ JSON (for system upload)

File with: Tax Authority (FVO)
```

**FVO Declaration:**

```
Path: HR → Payroll → FVO Declaration → New

Fill in:
- Declaration Month
- Declaration Year
- Company

Load Employees:
✓ Select employees with dependents
✓ Enter number of dependents
✓ Calculate FVO amount

Submit to Government:
✓ File number generated
✓ Submission date recorded
```

### 4. Payroll Adjustments

**Overtime Adjustment:**

```
Path: HR → Payroll → Suriname Payroll Entry
Edit: Employee row
Update: Overtime Hours field
System: Auto-calculates overtime amount (1.5x rate)
```

**Bonus/Additional Income:**

```
Path: HR → Payroll → Suriname Salary Slip
Edit: Bonus field
System: Auto-calculates new net pay
```

---

## Employee Guide

### 1. Viewing Your Dashboard

**Path:** HR → Employee Dashboard

**Information Available:**
- 👤 Your Profile (Name, Designation, Department)
- 💰 Current Salary Information
  - Gross Salary
  - Deductions (Tax, Social Security)
  - Net Pay
- 📅 Leave Balance
  - Annual leave remaining
  - Sick leave remaining
  - Maternity leave remaining
- 📋 Recent Payslips (Last 3 months)
- 📜 Leave History

### 2. Viewing Current Payslip

**Step 1: Access Payslip**
```
Path: HR → Employee Dashboard
Section: "Recent Payslips"
Click: View Latest
```

**Step 2: Review Payslip Details**
```
Earnings:
- Basic Salary
- Allowances
- Overtime (if applicable)
- Bonuses (if applicable)

Deductions:
- Income Tax (Progressive)
- Social Security (2.5%)
- Other deductions

Net Pay:
- Final take-home amount
```

### 3. Downloading Payslip

**Step 1: Open Payslip**
```
Path: HR → Payroll → Suriname Salary Slip
Select: Your name's slip
```

**Step 2: Download**
```
Click: Print button
Select: Download as PDF
Save: To your computer
```

### 4. Applying for Leave

**Step 1: Create Leave Request**
```
Path: HR → Leave Management → Suriname Leave Request
Click: New
```

**Step 2: Fill Details**
```
Employee: [Auto-filled]
Leave Type: Select from dropdown
- Annual
- Sick
- Maternity
- Special

From Date: [Select]
To Date: [Select]
```

**Step 3: Submit**
```
Click: Save
Click: Submit

Wait for: Manager approval
Notification: Sent via email when approved/rejected
```

**Step 4: Track Leave Status**
```
Path: HR → Employee Dashboard
Section: "Leaves Pending Approval"
View: Current requests
```

### 5. Understanding Your Payslip

**Salary Breakdown:**

```
GROSS SALARY (SRD)
├── Basic Salary: 20,000
├── Housing Allowance: 3,000
├── Transport Allowance: 1,500
├── Meal Allowance: 500
└── Total Earnings: 25,000

DEDUCTIONS (SRD)
├── Income Tax: 1,560 (18% bracket for 25,000)
├── Social Security (2.5%): 625
└── Total Deductions: 2,185

NET PAY (SRD)
└── Take-home: 22,815
```

**Tax Calculation Example:**

```
Gross Salary: SRD 25,000

Tax Brackets (Progressive):
- First 2,646 @ 0% = SRD 0
- Next 11,356 (2,646-14,002) @ 8% = SRD 908.48
- Next 7,917 (14,003-21,920) @ 18% = SRD 1,424.06
- Remaining 3,080 (21,920-25,000) @ 28% = SRD 862.40

Total Tax: SRD 3,195 (approximately)
```

---

## FAQ

### Q: When will my payslip be ready?
**A:** Payslips are generated automatically after monthly payroll is submitted, usually by the 25th of the month.

### Q: How do I apply for leave?
**A:** Navigate to HR → Suriname Leave Request → New, fill in dates, and submit. Your manager will approve.

### Q: Can I download my payslip as PDF?
**A:** Yes! Open your payslip and click Print → Download as PDF.

### Q: What if I have a salary discrepancy?
**A:** Contact your HR Manager. They can adjust in the next payroll cycle.

### Q: How many annual leave days do I get?
**A:** 12-15 days per year after 1 full year of service.

### Q: Is maternity leave paid?
**A:** Yes! 12 weeks (84 days) of paid maternity leave.

### Q: What's the minimum wage in Suriname?
**A:** SRD 60 per hour as of 2026.

### Q: What deductions appear on my payslip?
**A:** Income Tax (progressive) and Social Security (2.5%).

---

## Best Practices

### For HR Managers:

✅ **Monthly Checklist:**
1. Verify all employees are active
2. Check attendance is complete
3. Review overtime hours
4. Verify salary structures
5. Process payroll by 25th
6. Generate salary slips
7. File tax declarations
8. File FVO declarations
9. Archive payroll records
10. Send analytics reports

✅ **Compliance Tips:**
- Keep 7 years of payroll records
- File taxes on time
- File FVO monthly
- Monitor minimum wage compliance
- Track leave entitlements
- Document all changes
- Regular audits

### For Employees:

✅ **Best Practices:**
1. Review payslip monthly
2. Report discrepancies immediately
3. Plan leave in advance
4. Check leave balance before requesting
5. Download & keep payslips
6. Update personal details with HR
7. Report time sheets on time
8. Keep contract copy

---

## Support & Help

**For Technical Issues:**
- Contact IT Support
- Email: support@company.com
- Phone: +597-XXX-XXXX

**For Payroll Questions:**
- Contact HR Manager
- Email: hr@company.com
- Payroll Officer: +597-XXX-XXXX

**For General Queries:**
- Employee Portal Help
- FAQ Section in Dashboard
- HR Handbook

---

**Last Updated:** May 3, 2026
**Version:** 1.0.0