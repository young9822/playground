import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.newsletter_page import NewsletterPage

class AccountPage(BasePage):
    """AccountPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        # locators
        self._locs = {
            'heading account': (By.CSS_SELECTOR, "#content > div:nth-child(1) > h2"),
            'heading order': (By.CSS_SELECTOR, "#content > div:nth-child(2) > h2"),
            'menu logout': (By.CSS_SELECTOR, "#column-right > div > a:nth-child(14)"),
            'heading logout': (By.CSS_SELECTOR, "#content > h1"),
            'button continue': (By.CSS_SELECTOR, "#content > div > a"),
            'icon subscription': (By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)"),
            'message success': (By.CSS_SELECTOR, "#account-account > div.alert.alert-success.alert-dismissible"),
        }

        self._msgs = {
            'title': 'My Account',
            'heading account': 'My Account',
            'heading order': 'My Orders',
            'heading logout': ' Account Logout',
            'success': 'Success',
        }

    def goto_subscription(self):
        # click subscription icon to move to newsletter subscription page
        self.get_el_clickable('icon subscription').click()
        time.sleep(3)
        return NewsletterPage(self.driver)