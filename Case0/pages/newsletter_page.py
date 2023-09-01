"""
newsletter_page.py: definition of NewsletterPage class
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class NewsletterPage(BasePage):
    """NewsletterPage class"""
    def __init__(self, driver):
        """__init__"""
        super().__init__(driver)

        self._locs = {
            'radio yes': (By.CSS_SELECTOR, "#content > form > fieldset > div > div > div:nth-child(1) > label"),
            'selection yes': (By.CSS_SELECTOR, "#input-newsletter-yes"),
            'radio no': (By.CSS_SELECTOR, "#content > form > fieldset > div > div > div:nth-child(2) > label"),
            'selection no': (By.CSS_SELECTOR, "#input-newsletter-no"),
            'button continue': (By.CSS_SELECTOR, "#content > form > div > div.float-right > input"),
        }