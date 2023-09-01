"""
test_category.py

Note
+ test 'shop by category' menu

"""
import pytest
import time

from pages.home_page import HomePage
from pages.laptops_page import LaptopsPage
from pages.macs_page import MacsPage
from tests.base_test import BaseTest

class TestCategory(BaseTest):
    """TestCategory class"""

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_category(self) -> None:
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
        homePage = HomePage(self.driver)

        # validate the title
        assert homePage.get_title() == homePage.get_msg('title')

        # move to laptop page
        laptopsPage :LaptopsPage = homePage.goto_category('category laptops')

        # check the heading
        assert laptopsPage.get_el('heading').is_displayed()
        assert laptopsPage.get_el('heading').text == laptopsPage.get_msg('heading')

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
        assert macsPage.get_el('heading').is_displayed()
        assert macsPage.get_el('heading').text == macsPage.get_msg('heading')

