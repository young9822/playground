import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.laptops_page import LaptopsPage
from pages.search_result_page import SearchResultPage
from utils.info import SiteInfo

class HomePage(BasePage):
    """HomePage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        # move to home page
        self.driver.get(SiteInfo.URL['home'])
        time.sleep(3)

        # locators
        self._locs = {
            'menu category': (By.CSS_SELECTOR, "#entry_217832 > a"),
            'category laptops': (By.CSS_SELECTOR, "#widget-navbar-217841 > ul > li:nth-child(6) > a"),
            'text dummy': (By.CSS_SELECTOR, "#entry_217838 > p > strong"),
            'text copyright': (By.CSS_SELECTOR, "#entry_217561 > p"),
            'textbox search': (By.CSS_SELECTOR, "#search > div.search-input-group.flex-fill > div.search-input.d-flex > div.flex-fill > input[type=text]"),
            'button search': (By.CSS_SELECTOR, "#search > div.search-button > button"),
        }

        self._msgs = {
            'title': 'Your Store',
            'dummy': 'This is a dummy website for Web Automation Testing',
            'copyright': '© LambdaTest - Powered by OpenCart',
        }
    
    # move to one of category pages
    def goto_category(self, category) -> LaptopsPage:
        self.get_el_clickable('menu category').click()
        time.sleep(3)
        self.get_el_clickable(category).click()
        time.sleep(3)
        return LaptopsPage(self.driver)

    # move to search result page
    def search(self, product :str) -> SearchResultPage:
        self.get_el('textbox search').clear()
        self.get_el('textbox search').send_keys(product)
        self.get_el_clickable('button search').click()
        time.sleep(3)
        return SearchResultPage(self.driver)

