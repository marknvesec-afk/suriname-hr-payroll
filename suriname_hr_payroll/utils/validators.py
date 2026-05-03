"""
Validation utilities for Suriname payroll
"""

import re
from frappe import _()


def validate_phone_number(phone: str) -> bool:
    """
    Validate Suriname phone number format
    Suriname uses +597 country code
    """
    pattern = r"^(\+597|0)?[0-9]{6,8}$"
    return bool(re.match(pattern, phone.replace(" ", "").replace("-", "")))


def validate_id_number(id_num: str) -> bool:
    """
    Validate Suriname ID number format
    """
    # Basic validation - Suriname ID format varies
    return len(id_num.replace("-", "")) >= 8


def validate_dutch_contract_language(contract_text: str) -> bool:
    """
    Basic check if contract contains Dutch language
    """
    dutch_keywords = ["werkgeving", "salaris", "werktijden", "ziekte", "vakantie"]
    text_lower = contract_text.lower()
    return any(keyword in text_lower for keyword in dutch_keywords)