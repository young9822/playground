"""
test_overlapped_element.py
Overlapped Element: Entering text to a partially visible element may require scrolling it into view.

[Scenario]
Enter 'myid' in id field and 'myname' in name field

[Young's comment]
Sometimes, a creative way is required to break through a barrier. But with Playwright, it works without any additional action.

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_overlapped_element_by_playwright(BasePage):
    page :Page = BasePage

    # go to Overlapped Element page
    selection = 'Overlapped Element'
    page.get_by_text(selection, exact=True).click()
    expect(page).to_have_title(selection)

    # enter 'myid' to the id field
    page.get_by_placeholder("Id").fill("myid")
    expect(page.get_by_placeholder("Id")).to_have_value("myid")

    # enter 'myname' to the name field without scrolling the inner scrollbar
    page.get_by_placeholder("Name").fill("myname")
    expect(page.get_by_placeholder("Name")).to_have_value("myname")

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

@pytest.mark.selenium_only
def test_overlapped_element_by_selenium(driver):
    # go to Overlapped Element page
    driver.find_element(By.CSS_SELECTOR, "[href='/overlapped']").click()
    assert driver.title == 'Overlapped Element'

    # enter 'myid' to the id field
    driver.find_element(By.CSS_SELECTOR, "input#id").send_keys("myid")
    assert driver.find_element(By.CSS_SELECTOR, "input#id").get_attribute('value') == "myid"

    # scroll down before entering the name
    # as no way to locate the inner scrollbar
    # used mouse and keyboard to scroll
    driver.find_element(By.CSS_SELECTOR, "[style~='scroll;']").click()
    ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(1)   # fail without sleep

    # enter 'myname' to the name field
    driver.find_element(By.CSS_SELECTOR, "input#name").send_keys("myname")
    
    assert driver.find_element(By.CSS_SELECTOR, "input#name").get_attribute('value') == "myname"
    
    