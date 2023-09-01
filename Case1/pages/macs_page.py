"""
macs_page.py: definition of Macs page class
"""
from pages.base_page import BasePage
from playwright.sync_api import Page

class MacsPage(BasePage):
    """MacsPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'heading': self.page.get_by_role('heading', name='Macs'),
        }

        self._msgs = {
            'heading': 'Macs'
        }