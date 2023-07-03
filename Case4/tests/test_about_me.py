"""
test_about_me.py

[Scenario]
Click each tab and check if the title are correct

[Young's comment]
simple and easy one

"""

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy

def test_about_me(SetupiOS):
    driver: WebDriver = SetupiOS

    # check home view with title
    elTitle = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='All About')
    assert elTitle.text == 'All About'

    elName = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='My Name')
    assert elName.text == 'My Name'

    # move to story view
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Story').click()

    # check story view with title
    elTitle = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='My Story')
    assert elTitle.text == 'My Story'

    # move to favorite view
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Favorites').click()

    # check story view with title
    elTitle = driver.find_element(AppiumBy.IOS_PREDICATE, value="label == 'Favorites' AND name == 'Favorites' AND value == 'Favorites'")
    assert elTitle.text == 'Favorites'
    
    elName = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Hobbies')
    assert elName.text == 'Hobbies'

    elName = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Foods')
    assert elName.text == 'Foods'

    elName = driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Favorite Colors')
    assert elName.text == 'Favorite Colors'

    # move to fun facts view
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='Fun Facts').click()

    # check fun facts view with title
    elTitle = driver.find_element(AppiumBy.IOS_PREDICATE, value="label == 'Fun Facts' AND name == 'Fun Facts' AND value == 'Fun Facts'")
    assert elTitle.text == 'Fun Facts'
