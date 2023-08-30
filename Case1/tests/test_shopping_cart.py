"""
test_shopping_cart.py

Note
+ test product shopping cart feature

"""
import pytest
import re
import time
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
from pages.product_detail_page import ProductDetailsPage
from pages.shopping_cart_page import ShoppingCartPage
from tests.base_test import BaseTest
from utils.info import SiteInfo

class TestShoppingCart(BaseTest):
    """TestShoppingCart class"""
    page = BaseTest

    @pytest.mark.regression
    # @pytest.mark.e2e
    def test_shopping_cart(self, page :Page) -> None:
        """
        Validate product cart feature. Add 2 products in cart and remove all

        As a user, 
        when you add products in your cart,
        you can find them in your cart

        Validation
        1. heading
        2. notification window to move to your shopping cart
        3. product name and quantity in your shopping cart

        Mark:
        regression, e2e        
        """   
        siteInfo = SiteInfo()
        homePage = HomePage(page)

        # move to home page
        homePage.page.goto(siteInfo.homeURL)

        # enter 'iPhone' in search field and click the search button
        searchResultPage :SearchResultPage = homePage.search(siteInfo.searchItems['iphone']['name'])

        # if the 'heading' contains the search item name
        expect(searchResultPage.get_el('heading search')).to_be_visible()
        expect(searchResultPage.get_el('heading search')).to_contain_text(siteInfo.searchItems['iphone']['name'])

        # select the first item in search result        
        productDetailPage :ProductDetailsPage = searchResultPage.select_first_item()        
        
        # validate the name of selected item
        expect(productDetailPage.get_el('first item name')).to_be_visible()
        expect(productDetailPage.get_el('first item name')).to_have_text(siteInfo.searchItems['iphone']['name'])

        # click add to cart
        productDetailPage.get_el('button addtocart').click()

        # check the message of notification window
        expect(productDetailPage.get_el('popup message')).to_be_visible()
        expect(productDetailPage.get_el('popup message')).to_contain_text(productDetailPage.message['popup'])

        # click view cart button to move shopping cart page
        productDetailPage.get_el('button viewcart').click()

        # check if your product are in your cart
        shoppingCartPage = ShoppingCartPage(productDetailPage.page)
        expect(shoppingCartPage.get_el('td product first')).to_be_visible()
        expect(shoppingCartPage.get_el('td product first')).to_have_text(siteInfo.searchItems['iphone']['name'])
        expect(shoppingCartPage.get_el('td quantity first')).to_have_value(re.compile(r"[0-9]"))

        # click continue button to return to home page
        shoppingCartPage.get_el('button continue shopping').click()

        # enter 'iMac' in search field and click the search button
        searchResultPage :SearchResultPage = homePage.search(siteInfo.searchItems['imac']['name'])

        # if the 'heading' contains the search item name
        expect(searchResultPage.get_el('heading search')).to_be_visible()
        expect(searchResultPage.get_el('heading search')).to_contain_text(siteInfo.searchItems['imac']['name'])

        # select the first item in search result        
        productDetailPage :ProductDetailsPage = searchResultPage.select_first_item()        
        
        # validate the name of selected item
        expect(productDetailPage.get_el('first item name')).to_be_visible()
        expect(productDetailPage.get_el('first item name')).to_have_text(siteInfo.searchItems['imac']['name'])

        # click add to cart
        productDetailPage.get_el('button addtocart').click()

        # check the message of notification window
        expect(productDetailPage.get_el('popup message')).to_be_visible()
        expect(productDetailPage.get_el('popup message')).to_contain_text(productDetailPage.message['popup'])

        # click view cart button to move shopping cart page
        productDetailPage.get_el('button viewcart').click()

        # check if your product are in your cart
        shoppingCartPage = ShoppingCartPage(productDetailPage.page)
        expect(shoppingCartPage.get_el('td product second')).to_be_visible()
        expect(shoppingCartPage.get_el('td product second')).to_have_text(siteInfo.searchItems['imac']['name'])
        expect(shoppingCartPage.get_el('td quantity second')).to_have_value(re.compile(r"[0-9]"))

        # click continue button to return to home page
        shoppingCartPage.get_el('button continue shopping').click()

        time.sleep(2)

        """
        Move to shopping cart page and remove all products

        As a user, 
        when you go to shopping cart page,
        you can remove all products stored in your cart

        Validation
        1. heading
        2. message
        """
        shoppingCartPage = homePage.goto_shopping_cart()

        # delete all products stored in shopping cart
        shoppingCartPage.get_el('td delete first').click()
        shoppingCartPage.get_el('td delete second').click()

        # check if shopping cart is empty
        expect(shoppingCartPage.get_el('message empty')).to_be_visible()
        
        expect(shoppingCartPage.get_el('message empty')).to_contain_text(shoppingCartPage.messages['empty'])

        # return to home page
        shoppingCartPage.get_el('button continue').click()
        homePage.page = shoppingCartPage.page

        # validate the title
        expect(homePage.page).to_have_title(homePage.messages['title'])
        


        
