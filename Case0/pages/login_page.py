import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.account_page import AccountPage
from utils.info import SiteInfo

class LoginPage(BasePage):
    """LoginPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        # move to login page
        self.driver.get(SiteInfo.URL['login'])

        # locators
        self._locs = {
            'input email address': (By.CSS_SELECTOR, "#input-email"),
            'input password': (By.CSS_SELECTOR, "#input-password"),
            'button login': (By.CSS_SELECTOR, "input.btn.btn-primary"),
            'heading account': (By.CSS_SELECTOR, "#widget-navbar-217834 > ul > li:nth-child(6) > a"),
            'text warning': (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible"),
        }

        self._msgs = {
            'title': 'Account Login',
            'warning': 'Warning: No match for E-Mail Address and/or Password.',
        }

    def login(self, user :str) -> AccountPage:
        username, password = SiteInfo.userInfo[user]
        self.get_el('input email address').clear()
        self.get_el('input email address').send_keys(username)
        self.get_el('input password').send_keys(password)
        self.get_el('button login').click()
        time.sleep(3)
        return AccountPage(self.driver)