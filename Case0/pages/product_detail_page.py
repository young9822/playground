"""
product_detail_page.py: definition of product detail class
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    """SearchResultPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        self._locs = {
            'first item name': (By.CSS_SELECTOR, "#entry_216816 > h1"),
            'first item brand': (By.CSS_SELECTOR, "#entry_216826 > ul > li:nth-child(1) > a"),
            'button addtocart': None,
            'popup message': (By.CSS_SELECTOR, "#notification-box-top > div > div.toast-body > div.d-flex.mb-3.align-items-start > p"),
            'button viewcart': None,
        }

        self._msgs = {
            'popup': 'Success:',
        }

        