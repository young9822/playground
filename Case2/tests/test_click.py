"""
test_click.py
Click: Physical mouse click and DOM event emulated click are differently handled by browsers. There are still cases, with sometimes hardly identifiable reasons, when an event based click does not work. The solution for this problem is emulating physical mouse click. This page is specifically designed to ignore event based click.

[Scenario]
Click the button and click it again

[Young's comment]
Couldn't find any difficuly from both Playwright and Selenium

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_click_by_playwright(BasePage):
    page :Page = BasePage

    # go to Click page
    selection = 'Click'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # click the button
    page.get_by_role('button', name="Button That Ignores DOM Click Event").click()
    # and click again
    page.get_by_role('button', name="Button That Ignores DOM Click Event").click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_click_by_selenium(driver):
    # go to Click page
    driver.find_element(By.CSS_SELECTOR, "[href='/click']").click()
    assert driver.title == 'Click'

    # click the button
    driver.find_element(By.CSS_SELECTOR, "#badButton").click()
    # and click again
    driver.find_element(By.CSS_SELECTOR, "#badButton").click()
