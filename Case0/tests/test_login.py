"""
test_login.py

Note
+ test login feature with invalid and valid user information

"""
import pytest
import time
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestLogin(BaseTest):
    """TestHome class"""
    page = BaseTest

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_invalid_username(self, page :Page) -> None:
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
        siteInfo = SiteInfo()
        homePage = HomePage(page)
        
        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # move to login page
        loginPage :LoginPage = homePage.goto_login()

        # fill your email, password and click login button
        username = siteInfo.userInfo['invalidUsername']['username']
        password = siteInfo.userInfo['invalidUsername']['password']
        accountPage :AccountPage = loginPage.login(username, password)        

        # if the warning message is correct
        expect(loginPage.get_el('Warning')).to_contain_text(loginPage.messages['warning'])

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_invalid_password(self, page :Page) -> None:
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
        siteInfo = SiteInfo()
        homePage = HomePage(page)

        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # move to login page
        loginPage :LoginPage = homePage.goto_login()

        # fill your email, password and click login button
        username = siteInfo.userInfo['invalidPassword']['username']
        password = siteInfo.userInfo['invalidPassword']['password']
        accountPage :AccountPage = loginPage.login(username, password)     

        # if the heading of the account page has 'My Account'
        expect(loginPage.get_el('Warning')).to_contain_text(loginPage.messages['warning'])

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_login_valid(self, page :Page) -> None:
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
        siteInfo = SiteInfo()
        homePage = HomePage(page)

        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # move to login page
        loginPage :LoginPage = homePage.goto_login()

        # fill your email, password and click login button
        username = siteInfo.userInfo['valid']['username']
        password = siteInfo.userInfo['valid']['password']
        accountPage :AccountPage = loginPage.login(username, password)     

        # if the heading of the account page has 'My Account'
        expect(accountPage.get_el('heading account')).to_have_text('My Account')

        # if the heading of the account page has 'My Order'
        expect(accountPage.get_el('heading orders')).to_have_text('My Orders')

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
        time.sleep(3)   # sleep 3 seconds before logout

        # click logout item in side menu
        accountPage.get_el('menu logout').click()

        # check heading
        expect(accountPage.get_el('heading logout')).to_have_text('Account Logout')

        # click continue button
        accountPage.get_el('button continue').click()

        # validate the title directly
        expect(homePage.page).to_have_title(homePage.expectedTitle)
