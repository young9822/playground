"""
newsletter_page.py: definition of NewsletterPage class
"""
from pages.base_page import BasePage
from playwright.sync_api import Page

class NewsletterPage(BasePage):
    """NewsletterPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'radio yes': self.page.get_by_text('Yes', exact=True),
            'selection yes': self.page.locator("#input-newsletter-yes"),
            'radio no': self.page.get_by_text('No', exact=True),
            'selection no': self.page.locator("#input-newsletter-no"),
            'button continue': self.page.get_by_role('button', name='Continue'),
        }