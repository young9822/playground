"""
test_class_attribute.py
Class Attribute: Check that class attribute based XPath is well formed
but I used CSS selector in replacement of XPath as it's easy to use and simple

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_class_attribute_by_playwright(BasePage):
    page :Page = BasePage

    # go to Class Attribute page
    selection = 'Class Attribute'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    """
    By default, dialogs are auto-dismissed by Playwright, so you don't have to handle them. However, you can register a dialog handler before the action that triggers the dialog to either dialog.accept() or dialog.dismiss() it.
    """
    # setup a dialog handler to accept but it's not required in this case
    # page.on("dialog", lambda dialog: dialog.accept())
    # click the blue button
    page.locator('.btn-primary').click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_class_attribute_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='/classattr']").click()
    assert driver.title == 'Class Attribute'

    # click the blue button. css selector is better in this case
    driver.find_element(By.CSS_SELECTOR, "[class~='btn-primary']").click()

    # click ok in the alert
    driver.switch_to.alert.accept()