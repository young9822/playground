"""base_page.py"""
from selenium.webdriver import Safari
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    """BasePage is to contain common methods"""
    def __init__(self, driver :Safari|Chrome):
        """__init__"""
        self.driver = driver
        self._locs = {}
        self._msgs = {}

    def get_title(self) -> str:
        return self.driver.title
    
    def get_el(self, elName :str) -> WebElement:
        try:
            el = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self._locs[elName])
            )
        except Exception as e:
            print(f"Exception happened: {e}, {elName}")
        return el
    
    def get_el_clickable(self, elName :str) -> WebElement:
        try:
            el = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self._locs[elName])
            )
        except Exception as e:
            print(f"Exception happened: {e}, {elName}")
        return el
    
    def get_msg(self, msg :str) -> str:
        return self._msgs[msg]
