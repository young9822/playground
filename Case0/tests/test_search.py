"""
test_search.py

Note
+ test search feature and product detail page

"""
import pytest
import time

from pages.home_page import HomePage
from pages.laptops_page import LaptopsPage
from pages.macs_page import MacsPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestSearch(BaseTest):
    """TestSearch class"""

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_search_product(self) -> None:
        """
        Validate search feature

        Mark:
        regression, e2e   
        """      
        homePage = HomePage(self.driver)

        # validate the title
        assert homePage.get_title() == homePage.get_msg('title')

        """
        As a user, 
        when you connect to home page with correct url,
        and you enter 'iphone' in search field,
        you can find the search result in the screen

        Validation
        1. heading
        2. search field
        """
        # enter 'iPhone' in search field and click the search button
        searchResultPage = homePage.search(SiteInfo.searchItems['iphone']['name'])

        # if the 'heading' contains the search item name
        assert searchResultPage.get_el('heading search').is_displayed()
        assert SiteInfo.searchItems['iphone']['name'] in searchResultPage.get_el('heading search').text

        # if the placeholder of 'search field' has the search item name as a default
        assert searchResultPage.get_el('textbox search').get_attribute('value') == SiteInfo.searchItems['iphone']['name']

        """
        As a user,
        when you are in the result screen,
        and you click the first item,
        you can find the detail page

        Validation
        1. product name
        2. brand name
        """

        # select the first item in search result        
        productDetailPage = searchResultPage.select_first_item()        
        
        # validate the name of selected item
        assert productDetailPage.get_el('first item name').is_displayed()
        assert productDetailPage.get_el('first item name').text == SiteInfo.searchItems['iphone']['name']

        # validate the brand of selected item
        assert productDetailPage.get_el('first item brand').is_displayed()
        assert productDetailPage.get_el('first item brand').text == SiteInfo.searchItems['iphone']['brand']