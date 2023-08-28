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
            'radio yes': "#content > form > fieldset > div > div > div:nth-child(1) > label",
            'selection yes': "#input-newsletter-yes",
            'radio no': "#content > form > fieldset > div > div > div:nth-child(2) > label",
            'selection no': "#input-newsletter-no",
            'button continue': "#content > form > div > div.float-right > input",            
        }