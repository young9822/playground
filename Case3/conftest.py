"""This module is used to initialize a test"""
import pytest

from playwright.sync_api import Page, expect

@pytest.fixture()
def BasePage(page: Page):
    """base fixture for playwright"""
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title('The Internet')

    yield page

    print("Close driver")
    page.close()
