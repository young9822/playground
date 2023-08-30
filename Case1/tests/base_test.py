"""base_test.py"""
# pylint: disable=R0903
import pytest
from playwright.sync_api import Page

@pytest.mark.usefixtures("init_page")
class BaseTest:
    """BaseTest"""