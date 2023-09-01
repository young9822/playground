"""
macs_page.py: definition of Macs page class
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MacsPage(BasePage):
    """MacsPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        self._locs = {
            'heading': (By.CSS_SELECTOR, "#entry_212392 > h1"),
        }

        self._msgs = {
            'heading': 'Macs'
        }