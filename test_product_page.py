from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
import pytest
from .pages.basket_page import BasketPage
import time

@pytest.mark.parametrize('link', ProductPageLocators.PRODUCT_LINK_PARAMS)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)    
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)  # Without this function test does not work with Firefox. Firefox is so slow :(
    page.should_be_match_of_product_names_in_basket_message_and_product_page()
    page.should_be_basket_price_equal_to_added_product_price()

@pytest.mark.xfail(reason="bug won't be fixed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_basket_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.should_not_be_basket_message()

@pytest.mark.xfail(reason="bug won't be fixed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    success_message_should_disappear()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()
 
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, ProductPageLocators.PRODUCT_LINK)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()))
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
        page.open()
        page.should_not_be_basket_message()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLocators.PRODUCT_LINK)
        page.open()
        page.add_product_to_basket()
        page.should_be_match_of_product_names_in_basket_message_and_product_page()
        page.should_be_basket_price_equal_to_added_product_price()