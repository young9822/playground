"""collection of test data"""
# pylint: disable=R0903
class HomeInfo:
    """for home page"""
    urlHome = "https://ecommerce-playground.lambdatest.io/"
    search_items = {
        "iphone": {
            "name": "iPhone",
            "brand": "Apple",
            "product_code": "product 11"
        },
    }

class LoginInfo:
    """for login page"""
    urlLogin = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
    email = "siglab@naver.com"
    password = "younglee"
