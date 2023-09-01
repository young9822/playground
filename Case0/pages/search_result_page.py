"""
search_result_page.py: definition of SearchResultPage class
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_detail_page import ProductDetailsPage

class SearchResultPage(BasePage):
    """SearchResultPage class which has locators and methods for 'Login' page"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        self._locs = {
            'heading search': (By.CSS_SELECTOR, "#entry_212456 > h1"),
            'textbox search': (By.CSS_SELECTOR, "#input-search"),
            'first item': (By.CSS_SELECTOR, "#entry_212469 > div > div:nth-child(1) > div > div.caption > h4 > a"),
        }
    
    def select_first_item(self):
        self.get_el('first item').click()
        time.sleep(3)
        return ProductDetailsPage(self.driver)