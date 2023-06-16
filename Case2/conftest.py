"""This module is used to initialize a test"""
import pytest
from utilities import TestInfo

from playwright.sync_api import Page, expect

@pytest.fixture()
def BasePage(page: Page):
    # """base fixture for playwright"""
    # webkit = playwright.webkit
    # browser = webkit.launch()
    # # create a new incognito browser context
    # context = browser.new_context()
    # # create a new page inside context.
    # page = context.new_page()
    page.goto(TestInfo.HOME_URL)
    expect(page).to_have_title('UI Test Automation Playground')

    yield page

    print("Close driver")
    page.close()

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver(request):
    """base fixture for selenium: initialize a webdriver for chrome"""
    chrome_service = Service(ChromeDriverManager().install())
    # chrome_options = Options()
    # options = [
    #     # "--headless",
    #     "--disable-gpu",
    #     # "--windows-size=1920,1200",
    #     "--ignore-certificate-errors",
    #     "--disable-extensions",
    #     "--no-sandbox",
    #     "--single-process",
    #     "--disable-dev-shm-usage"
    # ]
    # for option in options:
    #     chrome_options.add_argument(option)
    # driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver = webdriver.Chrome(service=chrome_service)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestInfo.HOME_URL)
    assert driver.title  == 'UI Test Automation Playground'

    yield driver

    print("Close driver")
    driver.quit()
