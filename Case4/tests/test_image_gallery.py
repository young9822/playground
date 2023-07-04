"""
test_image_gallery.py

[Scenario]
- Story 1
Click 8th photo(rainbow) to see it in detail
Click 'Image Gallery' button to go back to home screen

- Story 2
Click 22nd photo(another rainbow) to see it in detail
Click 'Image Gallery' button to go back to home screen

- Story 3
Click '+' button
Click Waterfall photo to include 
Click the second photo to see it in detail
Click 'Image Gallery' button to go back to home screen
Click Edit button
Click x of Waterfall photo to remove
Click Done button

[Young's comment]
story 3 blocked as it fails always by malfunction of simulator 

"""
import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy

import time

@pytest.mark.app_name('Image Gallery')
def test_about_me(ios_driver):
    driver: WebDriver = ios_driver

    elTitle = driver.find_element(AppiumBy.CLASS_NAME, value='XCUIElementTypeStaticText')
    assert elTitle.text == 'Image Gallery'

    # story 1
    # click 8th photo(rainbow) to see it in detail
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton[8]").click()
    time.sleep(2)
    # click 'Image Gallery' button to go back to home screen
    driver.find_element(AppiumBy.CLASS_NAME, value='XCUIElementTypeButton').click()
    time.sleep(2)

    # story 2
    # click 22nd photo(another rainbow) to see it in detail
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton[22]").click()
    time.sleep(2)
    # click 'Image Gallery' button to go back to home screen
    driver.find_element(AppiumBy.CLASS_NAME, value='XCUIElementTypeButton').click()
    time.sleep(2)

    """
    # story 3
    # click '+' button
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeButton[`label == \"Add\"`]").click()
    time.sleep(2)
    # click Waterfall photo
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value="Photo, August 09, 2012, 06:55").click()
    time.sleep(2)
    # click Waterfall photo to see it in detail
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton[1]").click()
    time.sleep(2)
    # click 'Image Gallery' button to go back to home screen
    driver.find_element(AppiumBy.CLASS_NAME, value='XCUIElementTypeButton').click()
    time.sleep(2)
    # click Edit button
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeOther[`label == \"Edit\"`]/XCUIElementTypeOther").click()
    time.sleep(2)
    # click x of Waterfall photo to remove
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeButton[`label == \"Close\"`][1]").click()
    time.sleep(2)
    # click Done button
    driver.find_element(AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeButton[`label == \"Done\"`]").click()
    time.sleep(2)
    """