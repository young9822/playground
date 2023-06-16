"""
test_overlapped_element.py
Overlapped Element: Entering text to a partially visible element may require scrolling it into view.

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_overlapped_element_by_playwright(BasePage):
    page :Page = BasePage

    # go to Overlapped Element page
    selection = 'Overlapped Element'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_overlapped_element_by_selenium(driver):
    # go to Overlapped Element page
    driver.find_element(By.CSS_SELECTOR, "[href='/overlapped']").click()
    assert driver.title == 'Overlapped Element'