"""
test_subscription.py

Note
+ test newsletter subscription

"""
import pytest
import time

from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.newsletter_page import NewsletterPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestSubscription(BaseTest):
    """TestSearch class"""

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_toggle_subscription(self) -> None:
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
        loginPage = LoginPage(self.driver)

        # validate the title
        assert loginPage.get_title() == loginPage.get_msg('title')

        # fill your email, password and click login button
        accountPage :AccountPage = loginPage.login('valid')

        # validate the title
        assert accountPage.get_title() == accountPage.get_msg('title')

        # click subscription icon to move to newsletter subscription page
        newsletterPage :NewsletterPage = accountPage.goto_subscription()

        # get current selection of newsletter subscription
        curSelYes = newsletterPage.get_el('selection yes').get_attribute('checked')
        
        # toggle the radio button
        if curSelYes == 'true':
            newsletterPage.get_el_clickable('radio no').click()
            mySelection = 'No'
        else:   # else click 'Yes' radio button
            newsletterPage.get_el_clickable('radio yes').click()
            mySelection = 'Yes'
        time.sleep(3)
        
        # click 'Continue' button
        newsletterPage.get_el_clickable('button continue').click()
        time.sleep(3)

        # check success message
        assert accountPage.get_el('message success').is_displayed()
        assert accountPage.get_msg('success') in accountPage.get_el('message success').text

        # click subscription icon to move to newsletter subscription page
        newsletterPage :NewsletterPage = accountPage.goto_subscription()

        # validate my selection again
        curSelYes = newsletterPage.get_el('selection yes').get_attribute('checked')
        if mySelection == 'Yes':
            assert curSelYes == 'true'
        else:
            assert curSelYes == None
