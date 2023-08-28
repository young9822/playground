"""
search_result_page.py: definition of SearchResultPage class
"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.product_detail_page import ProductDetailsPage

class SearchResultPage(BasePage):
    """SearchResultPage class which has locators and methods for 'Login' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'heading': "#entry_212456 > h1",
            'search field': "#input-search",
            'first item': "#entry_212469 > div > div:nth-child(1) > div > div.caption > h4 > a",
        }
    
    def select_first_item(self):
        self.get_el('first item').click()
        return ProductDetailsPage(self.page)