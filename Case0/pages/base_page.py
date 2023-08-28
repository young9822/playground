"""base_page.py"""
from playwright.sync_api import Page, expect

class BasePage:
    """BasePage is to contain common methods"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page
        self._loocs = {}

    def get_el(self, elName :str) -> Page.locator:
        return self.page.locator(self._locs[elName])

    def check_title(self, title):
        """check a title of this page"""
        return self.page.title() == title