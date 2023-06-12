"""item_page.py"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.test_data import HomeInfo

class ItemDetailPage(BasePage):
    """locators and methods for item detail page"""
    # locators
    selected_item_locators = {
        'name': (By.CSS_SELECTOR, "#entry_216816 > h1"),
        'brand': (By.CSS_SELECTOR, "#entry_216826 > ul > li:nth-child(1) > a"),
        'product_code': (By.CSS_SELECTOR, "#entry_216820 > ul > li > span:nth-child(2)")
    }

    # properties
    def get_expected_name_from_selected_item(self):
        """return the name of selected item"""
        return HomeInfo.search_items["iphone"]["name"]

    def get_expected_brand_from_selected_item(self):
        """return the brand of selected item"""
        return HomeInfo.search_items["iphone"]["brand"]
