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
    page :Page = BasePage

    # go to Sample App page
    selection = 'Sample App'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    """
    Fill in and submit the form. For successfull login 
    use any non-empty user name and `pwd` as password.
    """
    # fill the login name and password
    page.get_by_placeholder("User Name").click()
    page.get_by_placeholder("User Name").fill("Young")
    page.get_by_placeholder("********").fill("pwd")
    # page.screenshot(path="screenshot2.png")
    # expect(page.get_by_placeholder("User Name")).to_have_value("Young")
    # expect(page.get_by_placeholder("***")).to_have_value("pwd")
    
    # click the login button
    page.get_by_role("button", name="Log In").click()
    # click the welcome message to validate
    page.get_by_text("Welcome, Young!").click()
    
# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_sample_app_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='/sampleapp']").click()
    assert driver.title == 'Sample App'

    # fill the login name and password
    driver.find_element(By.CSS_SELECTOR, \
        "input.form-control").send_keys("Young")
    driver.find_element(By.CSS_SELECTOR, \
        "input[type='password']").send_keys("pwd")
    # click the login button
    driver.find_element(By.CSS_SELECTOR, "#login").click()
    # click the welcome message to validate
    assert driver.find_element(By.CSS_SELECTOR, \
        "#loginstatus").text == "Welcome, Young!"
    
