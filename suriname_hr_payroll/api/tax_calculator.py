"""
Suriname Income Tax Calculator
Progressive tax brackets implementation
"""

from frappe import _

# Suriname Tax Brackets (2026) - in SRD
TAX_BRACKETS = [
    {"min": 0, "max": 2646, "rate": 0.0},
    {"min": 2646, "max": 14002, "rate": 0.08},
    {"min": 14003, "max": 21919, "rate": 0.18},
    {"min": 21920, "max": 32839, "rate": 0.28},
    {"min": 32840, "max": float("inf"), "rate": 0.38},
]


def calculate_tax(gross_salary: float) -> float:
    """
    Calculate progressive income tax for Suriname

    Args:
        gross_salary: Gross salary in SRD

    Returns:
        Calculated tax amount in SRD
    """
    if gross_salary <= 0:
        return 0

    tax = 0
    previous_max = 0

    for bracket in TAX_BRACKETS:
        if gross_salary <= bracket["min"]:
            break

        taxable_amount = min(gross_salary, bracket["max"]) - bracket["min"]
        tax += taxable_amount * bracket["rate"]
        previous_max = bracket["max"]

    return round(tax, 2)


def get_tax_bracket(gross_salary: float) -> dict:
    """
    Get the tax bracket for a given salary

    Args:
        gross_salary: Gross salary in SRD

    Returns:
        Dictionary with bracket info
    """
    for bracket in TAX_BRACKETS:
        if bracket["min"] <= gross_salary < bracket["max"]:
            return bracket
    return TAX_BRACKETS[-1]


def get_effective_tax_rate(gross_salary: float) -> float:
    """
    Calculate effective tax rate

    Args:
        gross_salary: Gross salary in SRD

    Returns:
        Effective tax rate as percentage
    """
    if gross_salary <= 0:
        return 0

    tax = calculate_tax(gross_salary)
    return round((tax / gross_salary) * 100, 2)