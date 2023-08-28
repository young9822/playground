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
                'My account': "#widget-navbar-217834 > ul > li:nth-child(6) > a",
                'E-Mail Address': "#input-email",
                'Password': "#input-password",
                'Login': "input.btn.btn-primary",
                'Warning': "#account-login > div.alert.alert-danger.alert-dismissible",
        }

        self.expecetedWarningMessage = 'Warning: No match for E-Mail Address and/or Password.'
    
    def login(self, username :str, password :str) -> AccountPage:
        self.get_el('E-Mail Address').clear()
        self.get_el('E-Mail Address').fill(username)
        self.get_el('Password').fill(password)
        self.get_el('Login').click()
        return AccountPage(self.page)
