import time

from .base_page import BasePage
from .locators import CartPageLocators


class CartPageElement(BasePage):
    def click_up_quantity(self):
        button = self.browser.find_element(*CartPageLocators.BUTTON_UP)
        self.button_click(button)

    def click_down_quantity(self):
        button = self.browser.find_element(*CartPageLocators.BUTTON_DOWN)
        self.button_click(button)

    def click_delete(self):
        button = self.browser.find_element(*CartPageLocators.BUTTON_DELETE)
        self.button_click(button)

    def get_product_name_in_cart(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text

    def get_product_price_in_cart(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text

    def get_product_quantity(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_QUANTITY).text

    def get_product_total_price(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_TOTAL_PRICE).text

    def get_products_total_price(self):
        products_total_price = self.browser.find_elements(*CartPageLocators.PRODUCT_TOTAL_PRICE)
        for product_total_price in products_total_price:
            yield product_total_price.text

    def get_total_price(self):
        return self.browser.find_element(*CartPageLocators.TOTAL_PRICE).text


class CartPage(CartPageElement):
    def correctly_product_name_in_cart(self, name_in_product_page):
        name_in_cart_page = self.get_product_name_in_cart()
        assert name_in_product_page == name_in_cart_page, "Имя товара в корзине не соответствует"

    def correctly_product_price_in_cart(self, price_in_product_page):
        price_in_cart_page = self.get_product_price_in_cart()
        assert price_in_product_page == price_in_cart_page, "Цена товара в корзине не соответствует"

    def should_be_up_quantity_and_correctly_product_total_price(self):
        quantity_before = int(self.get_product_quantity())
        product_price = float(self.get_product_price_in_cart())
        product_total_price = float(self.get_product_total_price())
        assert product_total_price == round(quantity_before * product_price, 3), 'Общая цена товара не соответсвует, до увеличения количества'
        i = 0
        while i < 5:
            self.click_up_quantity()
            quantity_after = int(self.get_product_quantity())
            product_total_price = float(self.get_product_total_price())
            assert quantity_after - quantity_before == 1, 'Количество товара не увеличилось'
            assert product_total_price == round(quantity_after * product_price, 3), 'Общая цена товара не соответсвует, после увеличения количества'
            quantity_before = quantity_after
            i += 1

    def should_be_down_quantity_and_correctly_product_total_price(self):
        quantity_before = int(self.get_product_quantity())
        product_price = float(self.get_product_price_in_cart())
        product_total_price = float(self.get_product_total_price())
        assert product_total_price == round(quantity_before * product_price, 3), 'Общая цена товара не соответсвует, до уменьшения количества'
        i = 0
        while i < 5 and quantity_before > 1:
            self.click_down_quantity()
            quantity_after = int(self.get_product_quantity())
            product_total_price = float(self.get_product_total_price())
            assert quantity_before - quantity_after == 1, 'Количество товара не увеличилось'
            assert product_total_price == round(quantity_after * product_price, 3), 'Общая цена товара не соответсвует, после увеличения количества'
            quantity_before = quantity_after
            i += 1

    def should_be_correctly_total_price(self):
        products_total_price = self.get_products_total_price()
        summ_product_total_price = 0
        for product_total_price in products_total_price:
            summ_product_total_price += float(product_total_price)
        total_price = float(self.get_total_price())
        print(total_price, summ_product_total_price)
        assert total_price == round(summ_product_total_price, 3), 'Общая цена корзины не соотвутствует цене всех товаров в ней'
