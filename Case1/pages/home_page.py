"""home_page.py: definition of HomePage class"""
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.laptops_page import LaptopsPage

class HomePage(BasePage):
    """HomePage class which has locators and methods for 'Home' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        # texts
        self.messages = {
            'title': 'Your Store',
            'dummy': 'This is a dummy website for Web Automation Testing',
            'copyright': '© LambdaTest - Powered by OpenCart'
        }
        
        # menu & buttons
        self.menus = [
                "Home",
                "Special",
                "Blog",        
        ]

        self.menuButtons = [
                "Mega Menu",
                "AddOns",
                "My account"
        ]

        # attributes
        self.attrs = {
                'menu': ['class', 'icon-left both nav-link'],
                'menuButton': ['data-toggle', 'dropdown'],
                'heading': ['class', 'module-title'],
        }

        # headings
        self.headings = [
                'TOP TRENDING CATEGORIES',
                'TOP PRODUCTS',
                'TOP COLLECTION',
                'FROM THE BLOG'
        ]

        # locators
        self._locs = {
            'menu category': self.page.get_by_role('button', name='Shop by Category'),
            'category laptops': self.page.get_by_role('link', name='Laptops & Notebooks'),
            'button shopping cart': self.page.locator("#entry_217825"),
            'button edit cart': self.page.get_by_role('button', name='Edit cart'),
        }

    # move to search result page
    def search(self, product :str) -> SearchResultPage:
        self.page.get_by_role('textbox', name='search').fill(product)
        self.page.get_by_role('button', name='search').click()
        return SearchResultPage(self.page)
    
    # move to login page
    def goto_login(self) -> LoginPage:
        self.page.get_by_role('button', name='My account').click()
        return LoginPage(self.page)
    
    # move to one of category pages
    def goto_category(self, category) -> LaptopsPage:
        self.get_el('menu category').click()
        self.get_el(category).click()
        return LaptopsPage(self.page)
    
    def goto_shopping_cart(self) -> ShoppingCartPage:
        self.get_el('button shopping cart').click()
        self.get_el('button edit cart').click()
        return ShoppingCartPage(self.page)
    
    def get_el_menu(self, menu :str):
        return self.page.get_by_role('link', name=menu).first
    
    def get_el_menu_button(self, menuButton :str):
        return self.page.get_by_role('button', name=menuButton)
    
    def get_el_dummy(self):
        return self.page.get_by_role('strong').nth(2)

    def get_el_heading(self, heading :str):
        return self.page.get_by_role('heading', name=heading)
