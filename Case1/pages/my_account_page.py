"""my_account_page: definition of MyAccountPage class for 'My Account' page"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyAccountPage(BasePage):
    """MyAccountPage which has locators and methods for 'My Account' page"""
    # locators
    my_account_locators = {
        "Edit your account information": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(1) > div > div > div:nth-child(1) > a"),
        "Change your password": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(1) > div > div > div:nth-child(2) > a"),
        "Modify your address book entries": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(1) > div > div > div:nth-child(3) > a"),
        "Modify your wish list": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(1) > div > div > div:nth-child(4) > a"),
        "Subscribe / unsubscribe to newsletter": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(1) > div > div > div:nth-child(5) > a")
    }
    my_orders_locators = {
        "View your order history": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(1) > a"),
        "Downloads": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(2) > a"),
        "Your Reward Points": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(3) > a"),
        "View your return requests": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(4) > a"),
        "Your Transactions": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(5) > a"),
        "Recurring payments": (By.CSS_SELECTOR, \
                    "#content > div:nth-child(2) > div > div > div:nth-child(6) > a")
    }
