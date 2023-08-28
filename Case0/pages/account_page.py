"""
account_page.py: definition of AccountPage class
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class AccountPage(BasePage):
    """AccountPage class which has locators and methods for 'Account' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locatorsAccount = {
                'heading account': "#content > div:nth-child(1) > h2",
                'heading orders': "#content > div:nth-child(2) > h2",
                'menu logout': "#column-right > div > a:nth-child(14)",
                'heading logout': "#content > h1",
                'button continue': "#content > div > a"
        }

    def get_el(self, elName :str):
        return self.page.locator(self._locatorsAccount[elName])