"""login_page: definition of LoginPage class"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage

class LoginPage(BasePage):
    """LoginPage class which have locators and methods for login page"""
    # locators
    my_account_menu = (By.CSS_SELECTOR, \
                    "#widget-navbar-217834 > ul > li:nth-child(6) > a > div > span")
    email_address_field = (By.CSS_SELECTOR, "#input-email")
    password_field = (By.CSS_SELECTOR, "#input-password")
    login_button = (By.CSS_SELECTOR, "input[value=\"Login\"]")
    warning_message = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")

    def set_email_address(self, email_address):
        """set email address"""
        self.set(self.email_address_field, email_address)

    def set_password(self, password):
        """set password"""
        self.set(self.password_field, password)

    def click_login_button(self):
        """click login button"""
        self.click(self.login_button)
        return MyAccountPage(self.driver)

    def login_workflow(self, email, password):
        """set email address and password and click login button"""
        self.set_email_address(email)
        self.set_password(password)
        return self.click_login_button()

    def get_warning_message(self):
        """get warning message for invalide credential"""
        return self.get_text(self.warning_message)
