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
            'td product first': self.page.locator("#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > a"),
            'td quantity first': self.page.locator("#content > form > div > table > tbody > tr > td:nth-child(4) > div > input"),
            'td delete first': self.page.locator("#content > form > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > button.btn.btn-danger"),
            'td product second': self.page.locator("#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a"),
            'td quantity second': self.page.locator("#content > form > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > input"),
            'td delete second': self.page.locator("#content > form > div > table > tbody > tr > td:nth-child(4) > div > div > button.btn.btn-danger"),
            'button continue shopping': self.page.get_by_role('link', name='Continue Shopping'),
            'message empty': self.page.locator("#content > p"),
            'button continue': self.page.get_by_role('link', name='Continue'),
        }

        self._msgs = {
            'empty': 'Your shopping cart is empty!'
        }