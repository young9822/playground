"""
login_page.py: definition of LoginPage class
"""
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.account_page import AccountPage
from utils.info import SiteInfo


class LoginPage(BasePage):
    """LoginPage class which has locators and methods for 'Login' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
                'My account': self.page.locator("#widget-navbar-217834 > ul > li:nth-child(6) > a"),
                'input email address': self.page.get_by_placeholder('E-Mail Address'),
                'input password': self.page.get_by_placeholder('Password'),
                'button login': self.page.get_by_role('button', name='Login'),
                'Warning': self.page.locator("div.alert.alert-danger.alert-dismissible"),
        }

        self.messages = {
            'warning': 'Warning: No match for E-Mail Address and/or Password.'
        }
    
    def login(self, username :str, password :str) -> AccountPage:
        self.get_el('input email address').clear()
        self.get_el('input email address').fill(username)
        self.get_el('input password').fill(password)
        self.get_el('button login').click()
        return AccountPage(self.page)
