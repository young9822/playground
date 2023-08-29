"""
test_search.py

Note
+ test search feature and product detail page

"""
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestSearch(BaseTest):
    """TestSearch class"""
    page = BaseTest

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_search_product(self, page :Page) -> None:
        """
        Validate search feature

        Mark:
        regression, e2e   
        """      
        siteInfo = SiteInfo()
        homePage = HomePage(page)

        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # validate the title
        expect(homePage.page).to_have_title(homePage.expectedTitle)

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
        searchResultPage = homePage.search(siteInfo.searchItems['iphone']['name'])

        # if the 'heading' contains the search item name
        expect(searchResultPage.get_el('heading search')).to_be_visible()
        expect(searchResultPage.get_el('heading search')).to_contain_text(siteInfo.searchItems['iphone']['name'])

        # if the 'search field' has the search item name as a default
        expect(searchResultPage.get_el('textbox search')).to_have_value(siteInfo.searchItems['iphone']['name'])

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
        expect(productDetailPage.get_el('first item name')).to_be_visible()
        expect(productDetailPage.get_el('first item name')).to_have_text(siteInfo.searchItems['iphone']['name'])

        # validate the brand of selected item
        expect(productDetailPage.get_el('first item brand')).to_have_text(siteInfo.searchItems['iphone']['brand'])