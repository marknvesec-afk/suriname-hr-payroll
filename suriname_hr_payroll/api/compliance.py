"""
Suriname Labor Law Compliance Utilities
Validation and compliance checking
"""

from datetime import datetime, timedelta
from frappe import _

# Suriname Labor Law Constants
MINIMUM_WAGE_PER_HOUR = 60.0  # SRD
MINIMUM_ANNUAL_LEAVE_DAYS = 12
MATERNITY_LEAVE_DAYS = 84  # 12 weeks
PATERNITY_LEAVE_DAYS = 0  # Not mandated
NOTICE_PERIODS = {
    "less_than_1_year": 1,  # 1 week
    "1_to_5_years": 4,  # 1 month
    "5_to_10_years": 8,  # 2 months
    "more_than_10_years": 12,  # 3 months
}
RECORD_RETENTION_YEARS = 7


def validate_minimum_wage(hourly_rate: float) -> bool:
    """
    Validate if hourly rate meets minimum wage requirement

    Args:
        hourly_rate: Hourly wage in SRD

    Returns:
        True if meets minimum, False otherwise
    """
    return hourly_rate >= MINIMUM_WAGE_PER_HOUR


def get_notice_period_days(years_of_service: int) -> int:
    """
    Get notice period in days based on years of service

    Args:
        years_of_service: Number of years employed

    Returns:
        Notice period in days
    """
    if years_of_service < 1:
        return NOTICE_PERIODS["less_than_1_year"]
    elif years_of_service < 5:
        return NOTICE_PERIODS["1_to_5_years"]
    elif years_of_service < 10:
        return NOTICE_PERIODS["5_to_10_years"]
    else:
        return NOTICE_PERIODS["more_than_10_years"]


def validate_leave_entitlement(tenure_months: int, leave_days_used: int) -> dict:
    """
    Validate annual leave entitlement

    Args:
        tenure_months: Months of continuous service
        leave_days_used: Days of leave already used

    Returns:
        Dictionary with entitlement info
    """
    # After 1 full year of service
    if tenure_months >= 12:
        entitled_days = MINIMUM_ANNUAL_LEAVE_DAYS
    else:
        # Pro-rata for partial year
        entitled_days = (tenure_months / 12) * MINIMUM_ANNUAL_LEAVE_DAYS

    return {
        "entitled_days": round(entitled_days, 2),
        "used_days": leave_days_used,
        "remaining_days": round(entitled_days - leave_days_used, 2),
        "is_compliant": leave_days_used <= entitled_days,
    }


def calculate_record_retention_end_date(payroll_date: datetime) -> datetime:
    """
    Calculate when payroll records can be safely deleted

    Args:
        payroll_date: Date of payroll processing

    Returns:
        Date when 7-year retention expires
    """
    return payroll_date + timedelta(days=365 * RECORD_RETENTION_YEARS)


def validate_fvo_declaration_required(employee_has_dependents: bool) -> bool:
    """
    Check if FVO (parental leave fund) declaration is required

    Args:
        employee_has_dependents: Whether employee has dependents

    Returns:
        True if FVO declaration required
    """
    return employee_has_dependents