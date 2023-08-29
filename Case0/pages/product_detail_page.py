"""
product_detail_page.py: definition of product detail class
"""
from playwright.sync_api import Page
from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    """SearchResultPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'first item name': "#entry_216816 > h1",
            'first item brand': "#entry_216826 > ul > li:nth-child(1) > a",
            'button addtocart': "#entry_216842 > button",
            'popup message': "#notification-box-top > div > div.toast-body > div.d-flex.mb-3.align-items-start > p",
            'button viewcart': "#notification-box-top > div > div.toast-body > div.form-row > div:nth-child(1) > a",
        }

        self.message = {
            'popup': 'Success:',
        }

        