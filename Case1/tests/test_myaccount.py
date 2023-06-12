"""test_myaccount.py"""
# pylint: disable=E1101
# pylint: disable=R0903
import time
import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import LoginInfo

class TestMyAccount(BaseTest):
    """TestMyAccount class"""
    @pytest.mark.regression
    @pytest.mark.e2e
    def test_myaccount_page(self):
        """
        Validate the following for 'My Account' page

        As a user, 
        when you login with proper email and password,
        you can find 'My Account' page which has the following

        Assertion
        1. title is 'My Account'
        2. My Account section has 5 menus with correct names
        3. My Orders section has 6 menus with correct names
        """
        self.driver.get(LoginInfo.urlLogin)
        self.driver.maximize_window()
        time.sleep(5)   # wait until it's clickable

        login_page = LoginPage(self.driver)
        myaccount_page = login_page.login_workflow(LoginInfo.email, LoginInfo.password)

        time.sleep(5)   # wait until it's clickable

        expected_title = "My Account"
        assert expected_title == myaccount_page.get_title()

        # validate texts of each menu in my account
        for key, value in myaccount_page.my_account_locators.items():
            assert key == myaccount_page.get_text(value)

        # validate texts of each menu in my account
        for key, value in myaccount_page.my_orders_locators.items():
            assert key == myaccount_page.get_text(value)
