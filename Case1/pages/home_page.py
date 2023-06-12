"""home_page.py: definition of HomePage class"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage
from utilities.test_data import HomeInfo

class HomePage(BasePage):
    """HomePage class which has locators and methods for 'Home' page"""
    # locators
    menu_locators = {
        "Home": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(1) > a > div > span"),
        "Special": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(2) > a > div > span"),
        "Blog": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(3) > a > div > span"),
        "Mega Menu": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(4) > a > div > span"),
        "AddOns": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(5) > a > div > span"),
        "My account": (By.CSS_SELECTOR, \
                "#widget-navbar-217834 > ul > li:nth-child(6) > a > div > span"),
    }

    dummy_locator = {"This is a dummy website for Web Automation Testing": \
        (By.CSS_SELECTOR, "#entry_217838 > p > strong")}

    search_field_locator = (By.CSS_SELECTOR, "#search > div.search-input-group.flex-fill > \
        div.search-input.d-flex > div.flex-fill > input[type=text]")
    search_button_locator = (By.CSS_SELECTOR, "#search > div.search-button > button")

    # expected texts
    expected_title = "Your Store"

    def search_item(self):
        """search an item"""
        self.set(self.search_field_locator, HomeInfo.search_items["iphone"]["name"])
        self.click(self.search_button_locator)
        return SearchResultPage(self.driver)
