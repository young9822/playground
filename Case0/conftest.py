"""This module is used to initialize a test"""
import pytest
from playwright.sync_api import Page

@pytest.fixture()
def init_page(page: Page):
    """base fixture for playwright"""    

    yield page

    print("Close driver")
    page.close()
