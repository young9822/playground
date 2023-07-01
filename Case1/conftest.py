"""This module is used to initialize a test"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType

@pytest.fixture(params=["chrome"])  # , "safari", "edge"])
def init_driver(request: pytest.FixtureRequest):
    """init_driver: initialize a webdriver for each browser and close it after a test"""
    if request.param == "safari":
        driver = webdriver.Safari()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else: # chrome
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--windows-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--single-process",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    request.cls.driver = driver
    print(f"Current browser: {request.param}")

    yield driver

    print("Close driver")
    driver.close()
