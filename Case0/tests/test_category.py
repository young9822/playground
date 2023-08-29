"""
test_category.py

Note
+ test 'shop by category' menu

"""
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.laptops_page import LaptopsPage
from pages.macs_page import MacsPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestCategory(BaseTest):
    """TestCategory class"""
    page = BaseTest

    @pytest.mark.regression
    @pytest.mark.e2e
    def test_category(self, page :Page) -> None:
        """
        Validate the following for 'Home' page

        As a user, 
        when you click 'laptops & notebooks' in category menu,
        you can move to 'Laptops' page

        Validation
        1. heading
        2. 

        Mark:
        regression, e2e        
        """   
        siteInfo = SiteInfo()
        homePage = HomePage(page)

        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # move to laptop page
        laptopsPage :LaptopsPage = homePage.goto_category('category laptops')

        # check the heading
        expect(laptopsPage.get_el('heading')).to_have_text(laptopsPage.messages['heading'])

        """
        As a user, 
        when you are in laptops page,
        and you click 'Macs',
        you can move to 'Macs' page

        Validation
        1. heading
        2. 

        Mark:
        regression, e2e        
        """
        # move to 'Macs' page
        macsPage :MacsPage = laptopsPage.goto_macs()

        # check the heading
        expect(macsPage.get_el('heading')).to_have_text(macsPage.messages['heading'])       
