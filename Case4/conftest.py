import pytest
import os
from pytest import FixtureRequest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from utilities.TestInfo import SetUPiOS

def get_desired_capabilities(appName :str) -> XCUITestOptions:
    options = XCUITestOptions()
    options.device_name = 'iPhone 14'
    options.platform_name = 'iOS'
    options.automation_name = 'XCUITest'
    options.language = 'en'
    options.locale = 'US'
    
    if appName is not None:
        if appName in SetUPiOS.myApps.keys():
            options.app = os.path.abspath(SetUPiOS.myApps.get(appName))
        elif appName in SetUPiOS.nativeApps.keys():   # iOS Navive apps
            options.app = SetUPiOS.nativeApps.get(appName)
        else:
            assert appName is None, "Wrong App name!"
    else:
        assert appName is not None, "App name missed!"

    return options

def create_ios_driver(appName):    
    options = get_desired_capabilities(appName)
    return webdriver.Remote(SetUPiOS.appium_server_url, options=options)

@pytest.fixture
def ios_driver_factory():
    return create_ios_driver

@pytest.fixture
def ios_driver(request: FixtureRequest):
    marker = request.node.get_closest_marker("app_name")
    if marker is None:
        assert marker is not None, 'The app name missed in marker'
    else:
        driver = create_ios_driver(marker.args[0])

    yield driver

    if driver is not None:
        driver.quit()
