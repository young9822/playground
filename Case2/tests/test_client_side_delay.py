"""
test_client_side_delay.py
Client Side Dealy: Some elements may appear after client-side time consuming JavaScript calculations

"""
import pytest

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_client_side_delay_by_playwright(BasePage):
    page :Page = BasePage

    # go to test input page
    selection = 'Client Side Delay'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    # click the button
    page.get_by_role('button', \
        name='Button Triggering Client Side Logic').click()
    # click the text to verify if it's disappeared
    # wonderful! passed by auto-waiting feature
    page.get_by_text('Data calculated on the client side.').click()

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.mark.selenium_only
def test_client_side_delay_by_selenium(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='/clientdelay']").click()
    assert driver.title == 'Client Side Delay'

    # click the button
    driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    # click the text to verify if it's disappeared
    # failed if no waiting
    # time.sleep() - bad choice    
    # driver.find_element(By.CSS_SELECTOR, "#content > p").click()
    # explicit wait with WebDriverWait
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content > p"))
        )
        element.click()
    except TimeoutException:
        print("Failed to load the element until timeout")
    except NoSuchElementException:
        print("No such element exception handled")