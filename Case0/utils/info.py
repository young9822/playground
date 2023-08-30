"""
info.py: definition of TestInfo class
"""
from os import environ
from playwright.sync_api import Page, expect

class SiteInfo():
    """LoginPage class which has locators and methods for 'Login' page"""
    def __init__(self):
        """__init__"""
        self.homeURL = "https://ecommerce-playground.lambdatest.io"

        # get email and password from os variables
        self.userInfo = {
            'valid': {
                'username': environ['TEST_EMAIL'], 
                'password': environ['TEST_PASSWORD']
            },
            'invalidUsername': {
                'username': 'invalid@example.io', 
                'password': environ['TEST_PASSWORD']
            },
            'invalidPassword': {
                'username': environ['TEST_EMAIL'], 
                'password': '1234qewradsf'
            }
        }

        self.searchItems = {
            'iphone': {
                'name': 'iPhone',
                'brand': 'Apple'
            },
            'imac': {
                'name': 'iMac',
                'brand': 'Apple'
            },
        }