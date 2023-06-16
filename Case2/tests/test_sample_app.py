"""
test_sample_app.py
Sample App: Demo application with dynamically 
generated element attributes

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_sample_app_by_playwright(BasePage):
    page = BasePage

    # go to test input page
    selection = 'Sample App'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    """
    Fill in and submit the form. For successfull login 
    use any non-empty user name and `pwd` as password.
    """
    # fill the login name and password
    page.get_by_placeholder("User Name", exact=True).fill("playwright")
    # page.screenshot(path="screenshot1.png")    
    page.get_by_placeholder("********").fill("pwd")
    page.screenshot(path="screenshot2.png")
    # click the login button
    page.get_by_role("button", name="Log In").click()
    # click the welcome message to validate
    # page.get_by_text("Welcome, playwright!").click()
    
# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_sample_app_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, \
        "#overview > div > div:nth-child(4) > div:nth-child(2) > h3 > a").click()
    assert driver.title == 'Sample App'

    # fill the login name and password
    driver.find_element(By.CSS_SELECTOR, \
        "input.form-control").send_keys("playwright")
    driver.find_element(By.CSS_SELECTOR, \
        "input[type='password']").send_keys("pwd")
    # click the login button
    driver.find_element(By.CSS_SELECTOR, "#login").click()
    # click the welcome message to validate
    assert driver.find_element(By.CSS_SELECTOR, \
        "#loginstatus").text == "Welcome, playwright!"
    
