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
            'heading account': self.page.get_by_role('heading', name='My Account'),
            'heading orders': self.page.get_by_role('heading', name='My Orders'),
            'menu logout': self.page.get_by_role('link', name='Logout'),
            'heading logout': self.page.get_by_role('heading', name='Account Logout'),
            'button continue': self.page.get_by_role('link', name='Continue'),
            'icon subscription': self.page.get_by_role('link', name='Subscribe'),
            'message success': self.page.locator("div.alert.alert-success.alert-dismissible"),
        }

        self._msgs = {
            'success': 'Success',
        }

    def goto_subscription(self):
        # click subscription icon to move to newsletter subscription page
        self.get_el('icon subscription').click()
        return NewsletterPage(self.page)