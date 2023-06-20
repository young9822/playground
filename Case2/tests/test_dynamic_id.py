"""
test_dynamic_id.py
Dynamic ID: Make sure you are not recording dynamic IDs of elements

[Scenario]
Click the button which has a dynamic id

[Young's comment]
In Selenium, CSS selector is a good choise to cover all cases

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_dynamic_id_by_playwright(BasePage):
    """test dynamic id page by playwright"""
    page :Page = BasePage

    # go to dynamic id page
    page.get_by_text('Dynamic ID', exact=True).click()
    expect(page).to_have_title('Dynamic ID')
    
    # click the dynamic button 
    page.get_by_role('button', name='Button with Dynamic').click()

# with selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium_only
def test_dynamic_id_by_selenium(driver): 
    """test dynamic id page by selenium"""       
    # go to dynamic id page
    driver.find_element(By.CSS_SELECTOR, "[href='/dynamicid']").click()
    assert driver.title == 'Dynamic ID'

    # click the dynamic id button
    # you can't use the id because it will be changed continuously
    driver.find_element(By.CSS_SELECTOR, "[class~='btn-primary']").click()
