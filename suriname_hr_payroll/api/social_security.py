"""
Suriname Social Security Calculations
Employee and Employer contributions
"""

from frappe import _

# Social Security Rates (2026)
EMPLOYEE_SS_RATE = 0.025  # 2.5% base rate
EMPLOYER_SS_RATE_MIN = 0.14  # 14% minimum
EMPLOYER_SS_RATE_MAX = 0.16  # 16% maximum


def calculate_employee_ss(gross_salary: float, rate: float = None) -> float:
    """
    Calculate employee social security contribution

    Args:
        gross_salary: Gross salary in SRD
        rate: Optional custom rate (defaults to 2.5%)

    Returns:
        Employee SS contribution in SRD
    """
    if gross_salary <= 0:
        return 0

    if rate is None:
        rate = EMPLOYEE_SS_RATE

    return round(gross_salary * rate, 2)


def calculate_employer_ss(gross_salary: float, rate: float = None) -> float:
    """
    Calculate employer social security contribution

    Args:
        gross_salary: Gross salary in SRD
        rate: Optional custom rate (defaults to 14-16%)

    Returns:
        Employer SS contribution in SRD
    """
    if gross_salary <= 0:
        return 0

    if rate is None:
        rate = EMPLOYER_SS_RATE_MIN  # Use minimum by default

    return round(gross_salary * rate, 2)


def calculate_total_ss_cost(gross_salary: float, employer_rate: float = None) -> dict:
    """
    Calculate total social security cost (employee + employer)

    Args:
        gross_salary: Gross salary in SRD
        employer_rate: Optional custom employer rate

    Returns:
        Dictionary with employee, employer, and total SS costs
    """
    employee_ss = calculate_employee_ss(gross_salary)
    employer_ss = calculate_employer_ss(gross_salary, employer_rate)

    return {
        "employee_ss": employee_ss,
        "employer_ss": employer_ss,
        "total_ss": employee_ss + employer_ss,
    }