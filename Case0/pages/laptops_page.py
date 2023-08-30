"""
laptops_page.py: definition of Laptops page class
"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.macs_page import MacsPage

class LaptopsPage(BasePage):
    """LaptopsPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'heading': self.page.get_by_role('heading', name='Laptops'),
            'macs': self.page.locator("#entry_212396 > div > a:nth-child(1) > figure"),
            'windows': self.page.locator("#entry_212396 > div > a:nth-child(2) > figure"),
        }

        self.messages = {
            'heading': 'Laptops'
        }

    def goto_macs(self) -> MacsPage:
        # move to 'Macs' page
        self.get_el('macs').click()
        return MacsPage(self.page)