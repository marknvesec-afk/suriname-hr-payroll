"""
Suriname Overtime Calculations
Handles overtime rates and calculations
"""

from frappe import _

# Overtime Rates
OVERTIME_STANDARD_RATE = 1.5  # 1.5x for standard overtime
OVERTIME_HOLIDAY_RATE = 2.0  # 2x for holiday overtime


def calculate_overtime(hourly_rate: float, hours: float, multiplier: float = None) -> float:
    """
    Calculate overtime pay

    Args:
        hourly_rate: Hourly wage in SRD
        hours: Number of overtime hours
        multiplier: Overtime multiplier (1.5x or 2x)

    Returns:
        Overtime payment in SRD
    """
    if hourly_rate <= 0 or hours <= 0:
        return 0

    if multiplier is None:
        multiplier = OVERTIME_STANDARD_RATE

    return round(hourly_rate * hours * multiplier, 2)


def calculate_overtime_from_attendance(
    daily_hours: list, hourly_rate: float, max_daily_hours: int = 8
) -> dict:
    """
    Calculate total overtime from daily attendance records

    Args:
        daily_hours: List of daily working hours
        hourly_rate: Hourly wage in SRD
        max_daily_hours: Maximum daily hours before overtime (default 8)

    Returns:
        Dictionary with overtime hours and payment
    """
    total_overtime_hours = 0

    for hours in daily_hours:
        if hours > max_daily_hours:
            total_overtime_hours += hours - max_daily_hours

    overtime_amount = calculate_overtime(hourly_rate, total_overtime_hours)

    return {"overtime_hours": total_overtime_hours, "overtime_amount": overtime_amount}


def calculate_weekly_overtime(weekly_hours: list, hourly_rate: float, max_weekly_hours: int = 40) -> dict:
    """
    Calculate overtime for weekly hours

    Args:
        weekly_hours: List of hours for each day of week
        hourly_rate: Hourly wage in SRD
        max_weekly_hours: Maximum weekly hours before overtime

    Returns:
        Dictionary with weekly overtime details
    """
    total_hours = sum(weekly_hours)
    overtime_hours = max(0, total_hours - max_weekly_hours)
    overtime_amount = calculate_overtime(hourly_rate, overtime_hours)

    return {"total_hours": total_hours, "overtime_hours": overtime_hours, "overtime_amount": overtime_amount}