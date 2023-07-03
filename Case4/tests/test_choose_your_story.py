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

[Young's comment]
Long but simple and easy one because of Accessibility ID

"""

import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.fixt_data('Choose Your Story')
def test_choose_your_story1(ios_driver):
    driver: WebDriver = ios_driver
    # story 1
    # click 'Front row!'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Front row!').click()
    # # click 'Trains'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Trains').click()
    # # click 'Sprinkles'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Sprinkles').click()
    # # click 'Pipe the decorations ...'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Pipe the decorations onto parchment paper. You can transfer them at the last minute.').click()
    # # check if you came in 3rd place
    result = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value="Good thinking!").text
    print(f"{result}")
    
