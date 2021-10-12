from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_MESSAGE_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE =(By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")