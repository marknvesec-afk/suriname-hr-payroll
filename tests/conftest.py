"""
Pytest configuration for Suriname HR/Payroll tests
"""

import pytest


@pytest.fixture
def sample_salary():
    """Sample salary for testing"""
    return 25000.00  # SRD


@pytest.fixture
def sample_hourly_rate():
    """Sample hourly rate for testing"""
    return 60.00  # SRD per hour (minimum wage)