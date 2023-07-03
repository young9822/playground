"""
test_choose_your_story.py

[Scenario]
- Story 1
Click 'Front row!'
Click 'Trains'
Click 'Sprinkles'
Click 'Pipe the decorations ...'
Check if you came in 3rd place

- Story 2
Click 'Front row!'
Click 'Trains'
Click 'Sprinkles'
Click 'Start decorating, ...'
Check if you finished in 6th place

- Story 3
Click 'Find somewhere in the middle'
Click 'Castles'
Click 'Marzipan figurines'

[Young's comment]
Long but simple and easy because of Accessibility ID

"""

import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.app_name('Choose Your Story')
def test_choose_your_story1(ios_driver):
    driver: WebDriver = ios_driver
    # story 1
    # click 'Front row!'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Front row!').click()
    # click 'Trains'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Trains').click()
    # click 'Sprinkles'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Sprinkles').click()
    # click 'Pipe the decorations ...'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Pipe the decorations onto parchment paper. You can transfer them at the last minute.').click()
    # check if you came in 3rd place
    result = driver.find_element(AppiumBy.IOS_PREDICATE, \
        value="type == 'XCUIElementTypeStaticText' AND name BEGINSWITH[c] 'Good'").text
    assert result.__contains__("You come in 3rd place!")

@pytest.mark.app_name('Choose Your Story')
def test_choose_your_story2(ios_driver):
    driver: WebDriver = ios_driver
    # story 2
    # click 'Front row!'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Front row!').click()
    # click 'Trains'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Trains').click()
    # click 'Sprinkles'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Sprinkles').click()
    # click 'Pipe the decorations ...'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Start decorating, you don’t have a minute to waste.').click()
    # check if you came in 6th place
    result = driver.find_element(AppiumBy.IOS_PREDICATE, \
        value="type == 'XCUIElementTypeStaticText' AND name BEGINSWITH 'Oh no'").text
    assert result.__contains__("you finish in 6th place")

@pytest.mark.app_name('Choose Your Story')
def test_choose_your_story3(ios_driver):
    driver: WebDriver = ios_driver
    # story 3
    # click 'Find somewhere in the middle'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Find somewhere in the middle').click()
    # click 'Castles'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Castles').click()
    # click 'Marzipan figurines'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Marzipan figurines').click()
    # check if you came in 8th place
    result = driver.find_element(AppiumBy.IOS_PREDICATE, \
        value="type == 'XCUIElementTypeStaticText' AND name CONTAINS '8th place.'").text
    assert result.__contains__("8th place")
    
