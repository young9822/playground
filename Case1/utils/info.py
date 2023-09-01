"""
info.py: definition of Information class
"""
class SiteInfo():
    """SiteInfo class"""
    def __init__(self):
        """__init__"""
        self.homeURL = "https://ecommerce-playground.lambdatest.io"

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