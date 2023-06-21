"""
test_verify_text.py
Verify Text: In general inner text of a DOM element is different from displayed on screen. Browsers normalize text upon rendering, but DOM nodes contain text as it is in HTML markup. Need to take this fact into account when searching for an element using it's text value.

[Scenario]
Find an element started with 'Welcome'

[Young's comment]
Maybe not easy for XPATH but easy for CSS Selector

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_verify_text_by_playwright(BasePage):
    page :Page = BasePage

    # go to Verify Text page
    selection = 'Verify Text'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # find an element started with 'Welcome'
    expect(page.get_by_text("Welcome UserName!", exact=True)).to_have_text("Welcome UserName!")

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.mark.selenium_only
def test_verify_text_by_selenium(driver :WebDriver):
    driver.find_element(By.CSS_SELECTOR, "[href='/verifytext']").click()
    assert driver.title == 'Verify Text'

    # find an element started with 'Welcome'
    verifyText = driver.find_element(By.CSS_SELECTOR, \
        "body > section > div > div.bg-primary > span").text
    assert verifyText == "Welcome UserName!"
        