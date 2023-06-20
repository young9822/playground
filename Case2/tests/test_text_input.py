"""
test_text_input.py
Text Input: Entering text with physical keyboard can be different from sending DOM events to an element. This page is specifically desined to illustrate this problem. There are cases when attempts to set a text via DOM events lead to nowhere and the only way to proceed is to emulate real keyboard input at OS level.

[Scenario]
Enter a text in text input field and click the button.
And click the button again which has new name

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

    # enter a text in text input field - fill() does not work
    new_name = "Thank you"
    page.get_by_placeholder("MyButton").type(new_name, delay=100)    
    # click the button
    page.get_by_text("Button That Should Change it's Name Based on Input Value").click()
    # click the button again which has new name
    page.get_by_role('button', name=new_name).click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_text_input_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='/textinput']").click()
    assert driver.title == 'Text Input'

    # enter a text in text input field
    new_name = 'Thank you'
    driver.find_element(By.CSS_SELECTOR, "[placeholder='MyButton']").send_keys(new_name)
    # click the button
    driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
    # click the button again which has new name
    driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

