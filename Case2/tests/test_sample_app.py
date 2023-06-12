"""
test_sample_app.py
Sample App: Demo application with dynamically 
generated element attributes

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_sample_app_by_playwright(BasePage):
    page = BasePage

    # go to test input page
    selection = 'Sample App'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    """
    Fill in and submit the form. For successfull login 
    use any non-empty user name and `pwd` as password.
    """
    # fill the login name and password
    page.get_by_placeholder("User Name", exact=True).fill("Young")
    page.screenshot(path="screenshot1.png")
    # page.get_by_placeholder("********").fill("pwd")
    # page.screenshot(path="screenshot2.png")
    # click the login button
    # page.get_by_role("button", name="Log In").click()
    # click the welcome message to validate
    # page.get_by_text("Welcome, Young!").click()
    