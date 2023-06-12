"""test_login.py"""
# pylint: disable=E1101
import time
import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities import LoginInfo

class TestLogin(BaseTest):
    """TestLogin class"""
    @pytest.mark.regression
    @pytest.mark.e2e
    def test_valid_credentials(self):
        """
        Validate the follwing for Login page

        As a user, 
        when you login with proper email and password,
        you can login successfully

        Assertion
        1. Validate the title to check if Login successfully with valid credential
        """
        self.driver.get(LoginInfo.urlLogin)
        self.driver.maximize_window()
        time.sleep(5)   # wait until it's clickable

        login_page = LoginPage(self.driver)
        login_page.login_workflow(LoginInfo.email, LoginInfo.password)

        time.sleep(5)   # wait until it's clickable

        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    @pytest.mark.regression
    def test_invalid_credentials(self):
        """
        Validate the follwing for Login page

        As a user, 
        when you login with incorrect email and password,
        you will fail to login and find the warning message

        Assertion
        1. Validate the title
        2. Validate if it shows correct warning message
        """
        self.driver.get(LoginInfo.urlLogin)
        self.driver.maximize_window()
        time.sleep(5)   # wait until it's clickable

        login_page = LoginPage(self.driver)
        login_page.login_workflow("for_test_1@email.com", "invalid")    # invalid credential

        print("'invalid_for_test1@email.com' entered as a email address")
        print("'invalid' entered as a password")
        print("Login button clicked")

        time.sleep(5)   # wait until it's clickable

        actual_title = login_page.get_title()
        assert actual_title == "Account Login"
        warning_message = login_page.get_warning_message()
        assert warning_message == "Warning: No match for E-Mail Address and/or Password."
