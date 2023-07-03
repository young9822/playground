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
