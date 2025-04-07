from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def product_name_in_cart(self, name_in_product_page):
        name_in_cart_page = self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text
        assert name_in_product_page == name_in_cart_page, "Имя товара в корзине не соответствует"


    def product_price_in_cart(self, price_in_product_page):
        price_in_cart_page = self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text
        assert price_in_product_page == price_in_cart_page, "Цена товара в корзине не соответствует"

