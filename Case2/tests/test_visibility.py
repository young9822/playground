"""
test_visibility.py
Visibility: Checking if element is visible on screen may be a non trivial task.

[Scenario]
Learn locators of all buttons. 
Press Hide button.
Determine if other buttons visible or not

[Young's comment]
Interesting exercise! The definition of 'hidden' is a bit different from each other.

"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_visibility_by_playwright(BasePage):
    page :Page = BasePage

    # go to Visibility page
    selection = 'Visibility'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # click all buttons except for Hide button
    # click Removed button
    page.get_by_role('button', name='Removed').click()
    # click Zero Width button
    page.get_by_role('button', name='Zero Width').click()
    # click Overlapped button
    page.get_by_role('button', name='Overlapped').click()
    # click Opacity 0 button
    page.get_by_role('button', name='Opacity 0').click()
    # click Visibility Hidden button
    page.get_by_role('button', name='Visibility Hidden').click()
    # click Display None button
    page.get_by_role('button', name='Display None').click()
    # click Offscreen button
    page.get_by_role('button', name='Offscreen').click()

    # click Hide button
    page.get_by_role('button', name='Hide').click()

    # hidden buttons
    expect(page.get_by_role('button', name='Removed')).to_be_hidden()
    expect(page.get_by_role('button', name='Zero Width')).to_be_hidden()
    expect(page.get_by_role('button', name='Visibility Hidden')).to_be_hidden()
    expect(page.get_by_role('button', name='Display None')).to_be_hidden()

    # not hidden buttons
    expect(page.get_by_role('button', name='Overlapped')).to_be_visible()
    expect(page.get_by_role('button', name='Opacity 0')).to_be_visible()
    expect(page.get_by_role('button', name='Offscreen')).to_be_visible()

# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.mark.selenium_only
def test_visibility_by_selenium(driver :WebDriver):
    # go to Visibility page
    driver.find_element(By.CSS_SELECTOR, "[href='/visibility']").click()
    assert driver.title == 'Visibility'

    # click all buttons except for Hide button
    # click Removed button
    driver.find_element(By.CSS_SELECTOR, "#removedButton").click()
    # click Zero Width button
    driver.find_element(By.CSS_SELECTOR, "#zeroWidthButton").click()
    # click Overlapped button
    driver.find_element(By.CSS_SELECTOR, "#overlappedButton").click()
    # click Opacity 0 button
    driver.find_element(By.CSS_SELECTOR, "#transparentButton").click()
    # click Visibility Hidden button
    driver.find_element(By.CSS_SELECTOR, "#invisibleButton").click()
    # click Display None button
    driver.find_element(By.CSS_SELECTOR, "#notdisplayedButton").click()
    # click Offscreen button
    driver.find_element(By.CSS_SELECTOR, "#offscreenButton").click()

    # click Hide button
    driver.find_element(By.CSS_SELECTOR, "#hideButton").click()

    # hidden buttons
    # can't locate 'removed' button
    # assert driver.find_element(By.CSS_SELECTOR, "#removedButton").is_displayed() == False
    assert driver.find_element(By.CSS_SELECTOR, "#zeroWidthButton").is_displayed() == False
    assert driver.find_element(By.CSS_SELECTOR, "#invisibleButton").is_displayed() == False
    assert driver.find_element(By.CSS_SELECTOR, "#notdisplayedButton").is_displayed() == False

    # hidden in selenium but not hidden in playwright
    assert driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed() == False
    assert driver.find_element(By.CSS_SELECTOR, "#offscreenButton").is_displayed() == False
    
    # not hidden buttons
    assert driver.find_element(By.CSS_SELECTOR, "#overlappedButton").is_displayed() == True
    
