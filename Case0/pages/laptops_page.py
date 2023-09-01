"""
laptops_page.py: definition of Laptops page class
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.macs_page import MacsPage

class LaptopsPage(BasePage):
    """LaptopsPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        self._locs = {
            'heading': (By.CSS_SELECTOR, "#entry_212392 > h1"),
            'macs': (By.CSS_SELECTOR, "#entry_212396 > div > a:nth-child(1) > figure"),
            'windows': (By.CSS_SELECTOR, "#entry_212396 > div > a:nth-child(2) > figure"),
        }

        self._msgs = {
            'heading': 'Laptops',
        }

    def goto_macs(self) -> MacsPage:
        # move to 'Macs' page
        self.get_el('macs').click()
        time.sleep(3)
        return MacsPage(self.driver)