"""
test_text_input.py
Text Input: Entering text into an edit field may not have effect

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_text_input_by_playwright(BasePage):
    page :Page = BasePage

    # go to test input page
    selection = 'Text Input'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    """
    Entering text with physical keyboard can be different from sending DOM events 
    to an element. This page is specifically desined to illustrate this problem. 
    There are cases when attempts to set a text via DOM events lead to nowhere 
    and the only way to proceed is to emulate real keyboard input at OS level.
    """
    # enter a text in text input field - fill() does not work
    new_name = "Thank you"
    page.get_by_placeholder("MyButton").type(new_name, delay=100)    
    # click the button
    page.get_by_text("Button That Should Change it's Name Based on Input Value").click()
    # click the button again with the new name
    page.get_by_role('button', name=new_name).click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_text_input_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, \
        "#overview > div > div:nth-child(2) > div:nth-child(4) > h3 > a").click()
    assert driver.title == 'Text Input'