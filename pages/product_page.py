from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def product_in_cart(self, product_name):
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART).text
        assert product_name_in_cart == product_name, "The product is not in the cart"

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_value(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_VALUE).text

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be. Method is_disappeared"

    def should_not_be_success_message_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be. Method is_not_element_present"

    def value_in_cart(self, product_value):
        product_value_in_cart = self.browser.find_element(*ProductPageLocators.VALUE_IN_CART).text
        assert product_value_in_cart == product_value, "The cart price does not match"
