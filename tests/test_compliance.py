"""
Tests for Suriname labor law compliance
"""

import pytest
from suriname_hr_payroll.api.compliance import (
    validate_minimum_wage,
    get_notice_period_days,
    validate_leave_entitlement,
)


class TestCompliance:
    """Test compliance with Suriname labor law"""

    def test_minimum_wage_valid(self, sample_hourly_rate):
        """Test minimum wage validation"""
        assert validate_minimum_wage(60.0) is True

    def test_minimum_wage_below(self):
        """Test below minimum wage"""
        assert validate_minimum_wage(50.0) is False

    def test_notice_period_less_1_year(self):
        """Notice period for less than 1 year"""
        days = get_notice_period_days(0.5)
        assert days == 1  # 1 week

    def test_notice_period_1_5_years(self):
        """Notice period for 1-5 years"""
        days = get_notice_period_days(3)
        assert days == 4  # 1 month

    def test_notice_period_10_plus_years(self):
        """Notice period for 10+ years"""
        days = get_notice_period_days(15)
        assert days == 12  # 3 months

    def test_leave_entitlement_full_year(self):
        """Leave entitlement after full year"""
        result = validate_leave_entitlement(12, 10)
        assert result["entitled_days"] == 12
        assert result["is_compliant"] is True

    def test_leave_entitlement_partial_year(self):
        """Leave entitlement for partial year"""
        result = validate_leave_entitlement(6, 5)
        assert result["entitled_days"] == 6.0
        assert result["is_compliant"] is True