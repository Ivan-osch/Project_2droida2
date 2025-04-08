from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .pages.products_page import ProductPage
from selenium.webdriver import ActionChains
import time
import pytest


def test_should_be_see_sort_in_products_page(browser):
    link = "https://novosibirsk.2droida.ru/"
    page = BasePage(browser, link)
    page.open()
    page.open_catalog()
    page.go_to_products_page()
    products_page = ProductPage(browser, browser.current_url)
    products_page.add_to_cart()
    products_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    actions = ActionChains(browser)  # смещение курсора с иконки Корзина
    actions.move_by_offset(200, 200)  # смещение курсора с иконки Корзина
    actions.perform()  # смещение курсора с иконки Корзина
    cart_page.should_be_up_quantity_and_correctly_product_total_price()
    #cart_page.should_be_down_quantity()