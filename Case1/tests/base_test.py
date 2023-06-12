"""base_test.py"""
# pylint: disable=R0903
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """BaseTest"""
