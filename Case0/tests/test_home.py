"""
test_home.py

Note
+ test basic structure of home page

"""
import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestHome(BaseTest):
    """TestHome class"""

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_valid_home(self) -> None:
        """
        Validate the following for 'Home' page

        As a user, 
        when you connect to home page with correct url,
        you can find home page

        Validation
        1. Title
        2. Dummy message
        3. Copyright text

        Mark:
        regression, e2e        
        """
        homePage = HomePage(self.driver)

        # validate the title
        assert homePage.get_title() == homePage.get_msg('title')

        # check the dummy message
        assert homePage.get_el('text dummy').is_displayed()
        assert homePage.get_el('text dummy').text == homePage.get_msg('dummy')

        # check the copyright message
        assert homePage.get_el('text copyright').is_displayed()
        assert homePage.get_el('text copyright').text == homePage.get_msg('copyright')