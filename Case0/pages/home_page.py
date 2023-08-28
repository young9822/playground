"""home_page.py: definition of HomePage class"""
from os import environ
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage
from playwright.sync_api import Page

class HomePage(BasePage):
    """HomePage class which has locators and methods for 'Home' page"""
    def __init__(self, page :Page):
        """__init__"""
        self.page = page

        # texts
        self.expectedTitle = "Your Store"
        self.dummyMessage = "This is a dummy website for Web Automation Testing"
        self.copyRightMsg = "© LambdaTest - Powered by OpenCart"

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

    def search(self, product :str):
        self.page.get_by_role('textbox', name='search').fill(product)
        self.page.get_by_role('button', name='search').click()
        return SearchResultPage(self.page)
    
    def goto_login(self):
        self.page.locator("#widget-navbar-217834 > ul > li:nth-child(6) > a").click()
        return LoginPage(self.page)
    
    def get_el_menu(self, menu :str):
        return self.page.get_by_role('link', name=menu).first
    
    def get_el_menu_button(self, menuButton :str):
        return self.page.get_by_role('button', name=menuButton)
    
    def get_el_dummy(self):
        return self.page.get_by_role('strong').nth(2)

    def get_el_heading(self, heading :str):
        return self.page.get_by_role('heading', name=heading)
