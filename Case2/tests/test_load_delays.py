"""
test_load_delays.py
Load Delays: Server response may often come with an unpredictable delay. So a test must be able to patiently wait for page loaded event from a browser.

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_load_delays_by_playwright(BasePage):
    page :Page = BasePage

    # go to Load Delays page    
    page.get_by_role('link', name='Load Delay').click()
    expect(page).to_have_title('Load Delays')
    
    # Ensure that a test is capable of waiting for a page to load    
    page.get_by_role('button', \
        name='Button Appearing After Delay').click()
    
# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_load_delay_by_selenium(driver):
    # go to Load Delays page
    driver.find_element(By.CSS_SELECTOR, "[href='/loaddelay']").click()
    assert driver.title == 'Load Delays'

    # Ensure that a test is capable of waiting for a page to load    
    assert driver.find_element(By.CSS_SELECTOR, \
        "button.btn.btn-primary").text == "Button Appearing After Delay"