"""base_test.py"""
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """BaseTest"""
    pass