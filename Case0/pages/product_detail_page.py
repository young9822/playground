"""
product_detail_page.py: definition of product detail class
"""
from pages.base_page import BasePage
from playwright.sync_api import Page

class ProductDetailsPage(BasePage):
    """SearchResultPage class which has locators and methods for 'Login' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'first item name': "#entry_216816 > h1",
            'first item brand': "#entry_216826 > ul > li:nth-child(1) > a",
        }

        