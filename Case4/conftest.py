import pytest
import os
from appium import webdriver

@pytest.fixture(autouse=False)
def SetupiOS():
    caps = dict(
        platformName = 'iOS',
        automationName = 'XCUITest',
        deviceName = 'iPhone 14',
        language='en',
        locale='US'
    )

    caps['app'] = os.path.abspath("/Users/youngh9822/Library/Developer/Xcode/DerivedData/About_Me-hcltlkrfevkgwuaqfcyarrxgmbnr/Build/Products/Debug-iphonesimulator/About Me.app")

    appium_server_url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, caps)

    yield driver

    if driver:
        driver.quit()