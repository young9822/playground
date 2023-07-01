"""This module is used to initialize a test"""
import pytest
from utilities import TestInfo

from playwright.sync_api import Page, expect

@pytest.fixture()
def BasePage(page: Page):
    """base fixture for playwright"""
    page.goto(TestInfo.HOME_URL)
    expect(page).to_have_title('UI Test Automation Playground')

    yield page

    print("Close driver")
    page.close()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

@pytest.fixture(scope="module")
def driver():
    """base fixture for selenium: initialize a webdriver for chromium"""
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = [
        "--headless=new",
        "--incognito",
        "--disable-gpu",
        "--start-maximized",
        # "--windows-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        # "--no-sandbox",
        "--single-process",
        # "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)
    
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    # driver = webdriver.Chrome(service=chrome_service)
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(TestInfo.HOME_URL)
    assert driver.title  == 'UI Test Automation Playground'

    yield driver

    print("Close driver")
    driver.quit()
