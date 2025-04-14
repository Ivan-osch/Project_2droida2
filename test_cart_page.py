from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .pages.products_page import ProductPage
from selenium.webdriver import ActionChains
import time
import pytest


#@pytest.mark.skip
def test_should_be_up_down_quantity_and_correctly_product_total_price(browser):
    link = "https://novosibirsk.2droida.ru/"
    number = 4
    page = BasePage(browser, link)
    page.open()
    page.open_catalog()
    page.go_to_products_page()
    products_page = ProductPage(browser, browser.current_url)
    products_page.add_to_cart(number)
    time.sleep(2)
    products_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    actions = ActionChains(browser)  # смещение курсора с иконки Корзина
    actions.move_by_offset(200, 200)  # смещение курсора с иконки Корзина
    actions.perform()  # смещение курсора с иконки Корзина
    cart_page.should_be_up_quantity_and_correctly_product_total_price()
    cart_page.should_be_down_quantity_and_correctly_product_total_price()

@pytest.mark.skip
def test_should_be_correctly_total_price(browser):
    link = "https://novosibirsk.2droida.ru/"
    numbers = [4, 5, 20, 1, 2, 25, 30, 31, 23]
    page = BasePage(browser, link)
    page.open()
    page.open_catalog()
    page.go_to_products_page()
    products_page = ProductPage(browser, browser.current_url)
    time.sleep(2)
    for number in numbers:
        products_page.add_to_cart(number)
    time.sleep(2)
    products_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    actions = ActionChains(browser)  # смещение курсора с иконки Корзина
    actions.move_by_offset(200, 200)  # смещение курсора с иконки Корзина
    actions.perform()  # смещение курсора с иконки Корзина
    cart_page.should_be_correctly_total_price()