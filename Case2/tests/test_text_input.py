"""
test_text_input.py
Text Input: Entering text into an edit field may not have effect

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_text_input_by_playwright(BasePage):
    page = BasePage

    # go to test input page
    selection = 'Text Input'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    # enter a text in text input field

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_text_input_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, \
        "#overview > div > div:nth-child(2) > div:nth-child(4) > h3 > a").click()
    assert driver.title == 'Text Input'