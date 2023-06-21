"""
test_progress_bar.py
Progress Bar: A web application may use a progress bar to reflect state of some lengthy process. Thus a test may need to read the value of a progress bar to determine if it is time to proceed or not.

[Scenario]
Clicks Start button and then waits for the progress bar to reach 75%. Then the test should click Stop. The less the differnce between value of the stopped progress bar and 75% the better your result.

[Young's comment]


"""
import pytest
import time

# with playwright
from playwright.sync_api import Page, expect

@pytest.mark.playwright_only
def test_progress_bar_by_playwright(BasePage):
    page :Page = BasePage

    # go to Verify Text page
    selection = 'Progress Bar'
    page.get_by_role('link', name=selection).click()
    expect(page).to_have_title(selection)

    # click the start button
    page.get_by_role('button', name='Start').click()

    # wait for the progress bar to reach 75%
    while True:
        curValue = int(page.get_by_role('progressbar').get_attribute('aria-valuenow'))
        if curValue >= 75:
            break
        else:
            time.sleep(0.01)

    # click the stop button
    page.get_by_role('button', name='Stop').click()

    # show the result
    print(page.locator('#result').inner_text())


# with selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.mark.selenium_only
def test_progress_bar_by_selenium(driver :WebDriver):
    driver.find_element(By.CSS_SELECTOR, "[href='/progressbar']").click()
    assert driver.title == 'Progress Bar'

    # click the start button
    driver.find_element(By.CSS_SELECTOR, "#startButton").click()
    
    # wait for the progress bar to reach 75%
    while True:
        curValue = int(driver.find_element(By.CSS_SELECTOR, \
            "#progressBar").get_attribute('aria-valuenow'))
        if curValue >= 75:
            break
        else:
            time.sleep(0.01)

    # click the stop button
    driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

    # show the result
    print(driver.find_element(By.CSS_SELECTOR, '#result').text)