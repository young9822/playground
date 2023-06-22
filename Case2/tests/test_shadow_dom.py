"""
test_shadow_dom.py
Shadow DOM: This is a page with a Shadow DOM component guid-generator. Using it one can generate a guid and copy it to the clipboard.

[Scenario]
Clicks on * and then on 'copy to clipboard' buttons.
Add an assertion step to compare the value from the clipboard with the on of the input field.

[Young's comment]


"""
import pytest
import pyperclip

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_shadow_dom_by_playwright(BasePage):
    page :Page = BasePage

    # go to Shadow DOM page
    selection = 'Shadow DOM'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # click * button
    page.locator('#buttonGenerate').click()
    # click 'copy to clipboard' button
    page.locator('#buttonCopy').click()
    # get the input value
    generatedGUID = page.locator('#editField').input_value()
    clipboardGUID = pyperclip.paste()
    assert generatedGUID == clipboardGUID

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.mark.selenium_only
def test_shadow_dom_by_selenium(driver :WebDriver):
    # go to Shadow DOM page
    driver.find_element(By.CSS_SELECTOR, "[href='/shadowdom']").click()
    assert driver.title == 'Shadow DOM'