"""base_page.py"""
from playwright.sync_api import Page, Locator

class BasePage:
    """BasePage is to contain common methods"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page
        self._locs = {}
    
    def get_el(self, elName :str) -> Locator:
        return self._locs[elName]
