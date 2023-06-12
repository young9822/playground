"""test_home.py"""
# pylint: disable=E1101, W0105
import time
import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.test_data import HomeInfo

class TestHome(BaseTest):
    """TestHome class"""
    @pytest.mark.regression
    @pytest.mark.e2e
    def test_valid_home(self):
        """
        Validate the following for 'Home' page

        As a user, 
        when you connect to home page with correct url,
        you can find home page

        Assertion
        1. Validate the title
        2. Validate the menu bar with proper names
        3. Validate the dummy message
        """
        self.driver.get(HomeInfo.urlHome)
        self.driver.maximize_window()
        time.sleep(5)

        home_page = HomePage(self.driver)

        # validate the title
        actual_title = home_page.get_title()
        assert actual_title == home_page.expected_title

        # validate the menu bar
        for key, value in home_page.menu_locators.items():
            assert key == home_page.get_text(value)

        # validate dummy message
        for key, value in home_page.dummy_locator.items():
            assert key == home_page.get_text(value)

    @pytest.mark.regression
    @pytest.mark.e2e
    def test_home_search(self):
        """
        Validate the following for 'Home' page

        As a user, 
        when you connect to home page with correct url,
        and you enter 'iphone' in search field,
        you can find the search result in the screen

        Assertion
        1. Validate the title
        2. Validate the search result
        """
        self.driver.get(HomeInfo.urlHome)
        self.driver.maximize_window()
        time.sleep(5)

        home_page = HomePage(self.driver)

        # validate the title
        actual_title = home_page.get_title()
        assert actual_title == home_page.expected_title

        # set a text in search field and get the text in search result
        search_result_page = home_page.search_item()
        search_result = search_result_page.get_text(search_result_page.search_result_field)
        print(search_result)
        time.sleep(5)
        assert HomeInfo.search_items["iphone"]["name"] in search_result

        """
        As a user,
        when you select the first item in search result,
        you can find the item page in detail

        Assertion
        1. Validate the title
        """

        # select the first item in search result
        item_detail_page = search_result_page.select_first_one()

        # validate the title
        actual_title = item_detail_page.get_title()
        expected_title = item_detail_page.get_expected_name_from_selected_item()
        assert actual_title == expected_title

        # validate the name of selected item
        actual_name = item_detail_page.get_text(item_detail_page.selected_item_locators['name'])
        expected_name = item_detail_page.get_expected_name_from_selected_item()
        assert actual_name == expected_name

        # validate the brand of selected item
        actual_brand = item_detail_page.get_text(item_detail_page.selected_item_locators['brand'])
        expected_brand = item_detail_page.get_expected_brand_from_selected_item()
        assert actual_brand == expected_brand
