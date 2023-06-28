"""
test_basic_auth.py
Basic Auth: Exercise basic authentication using a login dialog

[Scenario]
Click 'Basic Auth' link
Fill the user name and the password field with 'admin'
Click the login button
Check if 'Congraturation' message is appeared

[Young's comment]


"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_basic_auth_by_playwright(BasePage):
    page :Page = BasePage

    # go to Basic Auth page
    selection = 'Basic Auth'
    page.get_by_role('link', name=selection).click()

    # fill the user name and the password field with 'admin'
    