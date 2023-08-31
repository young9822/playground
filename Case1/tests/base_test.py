"""base_test.py"""
import pytest

@pytest.mark.usefixtures("init_page")
class BaseTest:
    """BaseTest"""