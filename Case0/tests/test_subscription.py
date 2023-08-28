"""
test_subscription.py

Note
+ test newsletter subscription

"""
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.newsletter_page import NewsletterPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestSubscription(BaseTest):
    """TestSearch class"""
    page = BaseTest

    @pytest.mark.regression
    @pytest.mark.e2e
    def test_enable_subscription(self, page :Page) -> None:
        """
        Validate the following for 'Home' page

        As a user, 
        when you login and move subscription page,
        you can turn my subscription on or off

        Validation
        1. success message
        2. selection of radio button

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

        # click subscription icon to move to newsletter subscription page
        newsletterPage :NewsletterPage = accountPage.goto_subscription()

        # get current selection of newsletter subscription
        curSelYes = newsletterPage.get_el('selection yes').get_attribute('checked')
        
        # if it's 'Yes', click 'No' radio button
        if curSelYes == 'checked':
            newsletterPage.get_el('radio no').click()
            mySelection = 'No'
        else:   # else click 'Yes' radio button
            newsletterPage.get_el('radio yes').click()
            mySelection = 'Yes'
        
        # click 'Continue' button
        newsletterPage.get_el('button continue').click()

        # check success message
        expect(accountPage.get_el('message success')).to_contain_text(accountPage.successMsg)

        # click subscription icon to move to newsletter subscription page
        newsletterPage :NewsletterPage = accountPage.goto_subscription()

        # validate my selection again
        curSelYes = newsletterPage.get_el('selection yes').get_attribute('checked')
        if mySelection == 'Yes':
            assert curSelYes == 'checked'
        else:
            assert curSelYes == None
