from selenium.webdriver.common.by import By
import pytest

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_MESSAGE_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE =(By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE =(By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    PRODUCT_LINK_PARAMS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="bug won't be fixed")),
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():    
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

class MainPageLocators():
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"