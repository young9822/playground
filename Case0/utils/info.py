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
                'username': environ.get('test_email'), 
                'password': environ.get('test_password')
            },
            'invalidUsername': {
                'username': 'invalid@example.io', 
                'password': environ.get('test_password')
            },
            'invalidPassword': {
                'username': environ.get('test_email'), 
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