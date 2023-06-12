"""
test_dynamic_id.py
Dynamic ID: Make sure you are not recording dynamic IDs of elements

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_dynamic_id_by_playwright(BasePage):
    """test dynamic id page by playwright"""
    page = BasePage

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
    driver.find_element(By.CSS_SELECTOR, \
        "#overview > div > div:nth-child(1) > div:nth-child(1) > h3 > a").click()
    assert driver.title == 'Dynamic ID'

    # click the dynamic id button
    # you can't use the id because it will be changed continuously
    driver.find_element(By.CSS_SELECTOR, \
        "body > section:nth-child(2) > div:nth-child(1) > button:nth-child(6)").click()
