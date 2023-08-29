"""
laptops_page.py: definition of laptops page class
"""
from pages.base_page import BasePage
from playwright.sync_api import Page

class LaptopsPage(BasePage):
    """LaptopsPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'heading': "#entry_212392 > h1",
        }

        self.messages = {
            'heading': 'Laptops'
        }