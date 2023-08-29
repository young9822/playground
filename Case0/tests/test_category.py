"""
test_category.py

Note
+ test 'shop by category' menu

"""
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.laptops_page import LaptopsPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestCategory(BaseTest):
    """TestCategory class"""
    page = BaseTest

    @pytest.mark.regression
    @pytest.mark.e2e
    def test_enable_subscription(self, page :Page) -> None:
        """
        Validate the following for 'Home' page

        As a user, 
        when you 'laptops & notebooks' in side menu,
        you can move to laptos page

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
        laptopsPage = homePage.goto_category('category laptops')

        # check the heading
        expect(laptopsPage.get_el('heading')).to_have_text(laptopsPage.messages['heading'])