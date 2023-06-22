"""
test_mouse_over.py
Mouse Over: Placing mouse over an element may change DOM and make the element unavailable

[Scenario]
Click 'Click me' link and click it again.
Make sure if click count is increasing by 2.

[Young's comment]
Playwright is easy to use and very simple and clear.

"""
import pytest
# import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_mouse_over_by_playwright(BasePage):
    page :Page = BasePage

    # go to Mouse Over page
    selection = 'Mouse Over'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # click the link, 'Click me'
    page.get_by_text('Click me').click()

    # click it again after 1 second
    # no consideration required for the change of the element 
    page.get_by_text('Click me').click()

    # make sure if the click count is increasing by 2
    expect(page.locator('#clickCount')).to_have_text('2')

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.mark.selenium_only
def test_mouse_over_by_selenium(driver :WebDriver):
    driver.find_element(By.CSS_SELECTOR, "[href='/mouseover']").click()
    assert driver.title == 'Mouse Over'

    # click the link, 'Click me'
    driver.find_element(By.CSS_SELECTOR, "a.text-primary").click()

    # click it again after 1 second
    # consider that the element is changed when placing mouose over
    # option 1
    # driver.find_element(By.CSS_SELECTOR, "a.text-warning").click()
    # option 2 - click any other place once and try it again
    driver.find_element(By.CSS_SELECTOR, "h4").click()
    driver.find_element(By.CSS_SELECTOR, "a.text-primary").click()

    # make sure if the click count is increasing by 2
    assert driver.find_element(By.CSS_SELECTOR, "#clickCount").text == '2'