"""
shopping_cart_page.py: definition of ShoppingCart page class
"""
from playwright.sync_api import Page
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    """ShoppingCartPage class"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        self._locs = {
            'td product first': "#content > form > div > table > tbody > tr > td:nth-child(2) > a",
            'td quantity first': "#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > input",
            'td delete first': "#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > button.btn.btn-danger",
            'td product second': "#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a",
            'td quantity second': "#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > input",
            'td delete second': "#content > form > div > table > tbody > tr > td:nth-child(4) > div > div > button.btn.btn-danger",
            'button continue shopping': "#content > div.buttons.d-flex > a.btn.btn-lg.btn-secondary.mr-auto",
            'message empty': "#content > p",
            'button continue': "#content > div > a",
        }

        self.messages = {
            'empty': 'Your shopping cart is empty!'
        }