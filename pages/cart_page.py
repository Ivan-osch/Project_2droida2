import time

from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def get_product_name_in_cart(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text

    def get_product_price_in_cart(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text

    def correctly_product_name_in_cart(self, name_in_product_page):
        name_in_cart_page = self.get_product_name_in_cart()
        assert name_in_product_page == name_in_cart_page, "Имя товара в корзине не соответствует"

    def correctly_product_price_in_cart(self, price_in_product_page):
        price_in_cart_page = self.get_product_price_in_cart()
        assert price_in_product_page == price_in_cart_page, "Цена товара в корзине не соответствует"

    def up_quantity(self):
        button = self.browser.find_element(*CartPageLocators.BUTTON_UP)
        button.click()

    def down_quantity(self):
        button = self.browser.find_element(*CartPageLocators.BUTTON_DOWN)
        button.click()

    def get_product_quantity(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_QUANTITY).text

    def get_product_total_price(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_TOTAL_PRICE).text

    def get_total_price(self):
        return self.browser.find_element(*CartPageLocators.TOTAL_PRICE).text

    def should_be_up_quantity_and_correctly_product_total_price(self):
        quantity_before = int(self.get_product_quantity())
        product_price = float(self.get_product_price_in_cart())
        product_total_price = float(self.get_product_total_price())
        assert product_total_price == quantity_before * product_price, 'Общая цена товара не соответсвует1'
        i = 0
        while i < 5:
            self.up_quantity()
            quantity_after = int(self.get_product_quantity())
            product_total_price = float(self.get_product_total_price())
            time.sleep(2)
            assert quantity_after - quantity_before == 1, 'Количество товара не увеличилось'
            assert product_total_price == quantity_after * product_price, 'Общая цена товара не соответсвует2'
            quantity_before = quantity_after
            i += 1

    def should_be_down_quantity(self):
        quantity_before = self.get_product_quantity()
        i = 0
        while i < 5 or quantity_before == 1:
            self.down_quantity()
            quantity_after = self.get_product_quantity()
            assert (int(quantity_before) - int(quantity_after)) == 1, 'Количество товара не уменьшилось'
            quantity_before = quantity_after
            i += 1
