"""
account_page.py: definition of AccountPage class
"""
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.newsletter_page import NewsletterPage

class AccountPage(BasePage):
    """AccountPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'heading account': "#content > div:nth-child(1) > h2",
            'heading orders': "#content > div:nth-child(2) > h2",
            'menu logout': "#column-right > div > a:nth-child(14)",
            'heading logout': "#content > h1",
            'button continue': "#content > div > a",
            'icon subscription': "#content > div:nth-child(1) > div > div > div:nth-child(5) > a",
            'message success': "#account-account > div.alert.alert-success.alert-dismissible",
        }

        self.successMsg = "Success"

    def goto_subscription(self):
        # click subscription icon to move to newsletter subscription page
        self.get_el('icon subscription').click()
        return NewsletterPage(self.page)