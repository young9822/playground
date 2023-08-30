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
            'first item name': self.page.locator("#entry_216816 > h1"),
            'first item brand': self.page.locator("#entry_216826 > ul > li:nth-child(1) > a"),
            'button addtocart': self.page.locator("#entry_216842").get_by_role('button', name='ADD TO CART'),
            'popup message': self.page.locator("#notification-box-top > div > div.toast-body > div.d-flex.mb-3.align-items-start > p"),
            'button viewcart': self.page.get_by_role('link', name='View Cart'),
        }

        self.message = {
            'popup': 'Success:',
        }

        