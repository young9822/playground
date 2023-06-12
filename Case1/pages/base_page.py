"""base_page.py"""

class BasePage:
    """BasePage is to contain common methods"""
    def __init__(self, driver):
        """__init__"""
        self.driver = driver

    def find(self, *locator):
        """find a element with locator"""
        return self.driver.find_element(*locator)

    def click(self, locator):
        """find and click a element with locator"""
        self.find(*locator).click()

    def set(self, locator, value):
        """find a element and send a text"""
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        """find a element with locator and get a text"""
        return self.find(*locator).text

    def get_title(self):
        """get a title of this page"""
        return self.driver.title
