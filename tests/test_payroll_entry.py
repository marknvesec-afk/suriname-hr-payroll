"""
Tests for payroll entry functions
"""

import pytest
from suriname_hr_payroll.api.social_security import calculate_employee_ss, calculate_employer_ss
from suriname_hr_payroll.api.tax_calculator import calculate_tax


class TestPayrollEntry:
    """Test payroll entry calculations"""

    def test_employee_ss_calculation(self, sample_salary):
        """Test employee social security calculation"""
        ss = calculate_employee_ss(sample_salary)
        assert ss == 625.0  # 25000 * 0.025

    def test_employer_ss_calculation(self, sample_salary):
        """Test employer social security calculation"""
        ss = calculate_employer_ss(sample_salary)
        assert ss >= 3500  # At least 14%

    def test_net_pay_calculation(self, sample_salary):
        """Test net pay calculation"""
        tax = calculate_tax(sample_salary)
        employee_ss = calculate_employee_ss(sample_salary)
        net_pay = sample_salary - tax - employee_ss
        assert net_pay > 0
        assert net_pay < sample_salary