"""This module is used to initialize a test"""
import pytest
from pytest import FixtureRequest
from selenium import webdriver
from selenium.webdriver.safari.webdriver import WebDriver as SafariWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChremeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=['safari'])
def init_driver(request :FixtureRequest):
    """base fixture for selenium"""
    if request.param == 'chrome':
        options = ChremeOptions()
        options.add_argument('headless')
        options.add_argument('--start-maximized')
        options.add_argument('incognito')
        driver :ChromeWebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # driver :ChromeWebDriver = webdriver.Chrome(options=options)
    else:
        driver :SafariWebDriver = webdriver.Safari()
        driver.maximize_window()

    driver.implicitly_wait(5)
    request.cls.driver = driver
    print(f"Browsser: {request.param}")

    yield

    print("Closed.")
    driver.close()