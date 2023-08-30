"""
test_home.py

Note
+ test basic structure of home page

"""
import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestHome(BaseTest):
    """TestHome class"""
    page = BaseTest

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_valid_home(self, page :Page) -> None:
        """
        Validate the following for 'Home' page

        As a user, 
        when you connect to home page with correct url,
        you can find home page

        Validation
        1. Title
        2. Menu bar if they have proper names
        3. Dummy message
        4. Headings
        5. Copyright text

        Mark:
        regression, e2e        
        """
        siteInfo = SiteInfo()
        homePage = HomePage(page)
        
        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # validate the title
        expect(homePage.page).to_have_title(homePage.messages['title'])

        # validate the menu bar
        for menu in homePage.menus:
            expect(homePage.get_el_menu(menu)).to_have_attribute(*homePage.attrs['menu'])
        
        for menuButton in homePage.menuButtons:
            expect(homePage.get_el_menu_button(menuButton)).to_have_attribute(*homePage.attrs['menuButton'])

        # validate dummy message
        expect(homePage.get_el_dummy()).to_have_text(homePage.messages['dummy'])

        # validate the headings
        for heading in homePage.headings:
            expect(homePage.get_el_heading(heading)).to_have_attribute(*homePage.attrs['heading'])

        # validate the copyright text
        expect(homePage.page.get_by_text('OpenCart')).to_have_text(homePage.messages['copyright'])


    


