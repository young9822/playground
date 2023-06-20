"""
test_scrollbars.py
Scrollbars: Scrolling an element into view may be a tricky task

[Scenario]
Click the hidden button

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_scrollbars_by_playwright(BasePage):
    """test scrollbars page by playwright"""
    page :Page = BasePage

    # go to scrollbars page
    page.get_by_text('Scrollbars').click()
    expect(page).to_have_title('Scrollbars')
    
    # click the hidden button
    # scroll is not required
    page.get_by_role('button', name='Hiding Button').click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_scrollbars_by_selenium(driver): 
    """test scrollbars page by selenium"""
    # go to scrollbars page
    driver.find_element(By.CSS_SELECTOR, "[href='/scrollbars']").click()
    assert driver.title == 'Scrollbars'

    # click the hidden button
    # scroll is not required, also
    driver.find_element(By.CSS_SELECTOR, "#hidingButton").click()



