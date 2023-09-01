"""
test_login.py

Note
+ test login feature with invalid and valid user information

"""
import pytest
import time

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    """TestLogin class"""
    
    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_invalid_username(self) -> None:
        """
        Invalid username

        As a user, 
        when you click login in the main menu of home page,
        and you fill invalid email, valid password and click login button in login page,
        you can find warning message

        Validation
        1. warning message

        Mark:
        regression, e2e        
        """        
        loginPage = LoginPage(self.driver)

        # validate the title
        assert loginPage.get_title() == loginPage.get_msg('title')

        # fill your email, password and click login button   
        accountPage :AccountPage = loginPage.login('invalidUsername')

        # if the warning message is correct
        assert loginPage.get_el('text warning').is_displayed()
        assert loginPage.get_msg('warning') in loginPage.get_el('text warning').text

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_invalid_password(self) -> None:
        """
        Invalid password

        As a user, 
        when you click login in the main menu of home page,
        and you fill valid email, invalid password and click login button in login page,
        you can find warning message

        Validation
        1. warning message

        Mark:
        regression, e2e        
        """
        loginPage = LoginPage(self.driver)

        # validate the title
        assert loginPage.get_title() == loginPage.get_msg('title')

        # fill your email, password and click login button
        accountPage :AccountPage = loginPage.login('invalidPassword')

        # if the heading of the account page has 'My Account'
        assert loginPage.get_el('text warning').is_displayed()
        assert loginPage.get_msg('warning') in loginPage.get_el('text warning').text

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_valid(self) -> None:
        """
        Validate login action

        As a user, 
        when you click login in the main menu of home page
        and you fill valid email, password and click login button in login page,
        you can find account page

        Validation
        1. heading

        Mark:
        regression, e2e        
        """
        loginPage = LoginPage(self.driver)

        # validate the title
        assert loginPage.get_title() == loginPage.get_msg('title')

        # fill your email, password and click login button
        accountPage :AccountPage = loginPage.login('valid')

        # validate the title
        assert accountPage.get_title() == accountPage.get_msg('title')

        # validate the heading
        assert accountPage.get_el('heading account').is_displayed()
        assert accountPage.get_el('heading account').text == accountPage.get_msg('heading account')
        assert accountPage.get_el('heading order').is_displayed()
        assert accountPage.get_el('heading order').text == accountPage.get_msg('heading order')

        """
        Validate logout action

        As a user, 
        when you are in login already,
        and you click logout in the menu,
        you can logout successfully

        Validation
        1. heading
        2. continue button
        """
        # click logout item in side menu
        accountPage.get_el('menu logout').click()
        time.sleep(3)

        # check heading
        assert accountPage.get_el('heading logout').is_displayed()
        assert accountPage.get_el('heading logout').text == accountPage.get_msg('heading logout')
        
        # click continue button
        accountPage.get_el('button continue').click()
        homePage = HomePage(accountPage.driver)

        time.sleep(3)

        # check title
        assert homePage.get_title() == homePage.get_msg('title')