"""search_result_page.py"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.item_detail_page import ItemDetailPage

class SearchResultPage(BasePage):
    """SearchResultPage which has locators and methods for search result page"""
    # locators
    search_result_field = (By.CSS_SELECTOR, "#entry_212456 > h1")
    item_locators = [
        (By.CSS_SELECTOR, \
            "#mz-product-grid-image-40-212469 > div > div.carousel-item.active > img"),
        (By.CSS_SELECTOR, \
            "#mz-product-grid-image-55-212469 > div > div.carousel-item.active > img")
    ]
    expected_title = "iphone"

    # methods
    def select_first_one(self):
        """select the first product"""
        self.click(self.item_locators[0])
        return ItemDetailPage(self.driver)
