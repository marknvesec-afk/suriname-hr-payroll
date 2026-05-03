"""
Tests for Suriname tax calculator
"""

import pytest
from suriname_hr_payroll.api.tax_calculator import calculate_tax, get_tax_bracket, get_effective_tax_rate


class TestTaxCalculator:
    """Test tax calculation functions"""

    def test_zero_salary(self):
        """Tax on zero salary should be zero"""
        assert calculate_tax(0) == 0

    def test_bracket_0_percent(self):
        """Salary in 0% bracket"""
        tax = calculate_tax(2000)
        assert tax == 0

    def test_bracket_8_percent(self, sample_salary):
        """Salary in 8% bracket"""
        # 14002 - 2646 = 11356 * 0.08 = 908.48
        tax = calculate_tax(14002)
        assert tax > 0

    def test_progressive_tax(self, sample_salary):
        """Test progressive tax calculation"""
        tax = calculate_tax(25000)
        assert tax > 0
        # Tax should increase with salary
        higher_tax = calculate_tax(35000)
        assert higher_tax > tax

    def test_get_effective_rate(self, sample_salary):
        """Test effective tax rate calculation"""
        rate = get_effective_tax_rate(sample_salary)
        assert 0 <= rate <= 100

    def test_negative_salary(self):
        """Negative salary should return zero tax"""
        assert calculate_tax(-5000) == 0