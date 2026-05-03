"""
Helper functions for Suriname payroll
"""

from datetime import datetime, timedelta
from frappe import _


def format_currency_srd(amount: float) -> str:
    """
    Format amount as Surinamese currency
    """
    return f"SRD {amount:,.2f}"


def get_fiscal_year_dates(year: int) -> dict:
    """
    Get fiscal year start and end dates
    Suriname fiscal year = calendar year
    """
    return {
        "start_date": datetime(year, 1, 1),
        "end_date": datetime(year, 12, 31),
    }


def is_public_holiday_suriname(date: datetime) -> bool:
    """
    Check if date is Suriname public holiday
    """
    public_holidays = [
        (1, 1),   # New Year
        (2, 25),  # Revolution Day
        (5, 1),   # Labour Day
        (7, 1),   # Emancipation Day
        (10, 10), # National Day
        (12, 25), # Christmas
        (12, 26), # Boxing Day
    ]

    return (date.month, date.day) in public_holidays


def calculate_business_days(start_date: datetime, end_date: datetime) -> int:
    """
    Calculate business days (excluding weekends)
    """
    business_days = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:  # Mon-Fri
            business_days += 1
        current_date += timedelta(days=1)

    return business_days