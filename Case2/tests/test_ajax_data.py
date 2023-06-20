"""
test_ajax_data.py
AJAX Data: An element may appaear on a page after processing of an AJAX request to a web server. A test should be able to wait for an element to show up.

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_ajax_data_by_playwright(BasePage):
    page :Page = BasePage

    # go to AJAX Data page
    selection = 'AJAX Data'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
    page.get_by_role('button', name="Button Triggering AJAX Request").click()
    page.get_by_text("Data loaded with AJAX get request.").click()

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.mark.selenium_only
def test_ajax_data_by_selenium(driver):
    # go to AJAX Data page
    driver.find_element(By.CSS_SELECTOR, "[href='/ajax']").click()
    assert driver.title == 'AJAX Data'

    # Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
    driver.find_element(By.CSS_SELECTOR, "button#ajaxButton").click()
    # fail if no wait
    # explicit wait with WebDriverWait
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        )
        assert element.text == "Data loaded with AJAX get request."
    except TimeoutException:
        print("Failed to load the element until timeout")
    except NoSuchElementException:
        print("No such element exception handled")
