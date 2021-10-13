from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver

class ProductPage(BasePage):

    # Check if all necessary buttons and information presented on the product page
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
    def should_be_product_name_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE_NAME), "Product name in the basket messege is not presented"
    def should_be_product_name_on_product_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PAGE_NAME), "Product name on the product page is not presented" 
    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Basket price is not presented" 
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"     
        
    # Add product to basket
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click() 
        
    # Check expected result after adding product to the basket    
    def should_be_match_of_product_names_in_basket_message_and_product_page(self):
        self.should_be_product_name_in_basket_message()
        self.should_be_product_name_on_product_page()
        product_name_in_basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_NAME).text
        product_name_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text
        assert product_name_in_basket_message == product_name_on_product_page, "Product name in the basket message does not match product name on the product page"        
    def should_be_basket_price_equal_to_added_product_price(self):
        self.should_be_basket_price()
        self.should_be_product_price()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == basket_price, "Produc t price in the basket message does not equal product price on the product page"
    
    # Negative checks
    def should_not_be_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not desappeared, but should be"
    
 
