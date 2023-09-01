from os import environ

class SiteInfo():
    """SiteInfo class"""
    URL = {
        'home': "https://ecommerce-playground.lambdatest.io",
        'login': "https://ecommerce-playground.lambdatest.io/index.php?route=account/login",
    }

    # get email and password from os variables
    userInfo = {
        'valid': (environ['TEST_EMAIL'], environ['TEST_PASSWORD']),
        'invalidUsername': ('invalid2@example.io', environ['TEST_PASSWORD']),
        'invalidPassword': (environ['TEST_EMAIL'], '1234qewradsf'),
    }

    searchItems = {
        'iphone': {
            'name': 'iPhone',
            'brand': 'Apple'
        },
        'imac': {
            'name': 'iMac',
            'brand': 'Apple'
        },
    }