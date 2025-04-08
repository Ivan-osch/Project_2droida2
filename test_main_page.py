from .pages.cart_page import CartPage
from .pages.base_page import BasePage
from .pages.products_page import ProductPage
import time
import pytest


@pytest.mark.skip
def test_should_be_see_sort_in_products_page(browser):
    link = "https://2droida.ru/"
    page = BasePage(browser, link)
    page.open()
    page.open_catalog()
    page.go_to_products_page()
    products_page = ProductPage(browser, browser.current_url)
    products_page.sort_by_increase()
    products_page.should_be_sort_by_increase()
    products_page.sort_by_decrease()
    products_page.should_be_sort_by_decrease()


def test_can_add_product_to_basket(browser):
    link = "https://novosibirsk.2droida.ru/"
    page = BasePage(browser, link)
    page.open()
    page.open_catalog()
    page.go_to_products_page()
    products_page = ProductPage(browser, browser.current_url)
    products_page.should_not_be_product_in_cart()
    products_page.add_to_cart()
    products_page.should_be_product_in_cart()
    name_in_product_page = products_page.get_product_name()
    price_in_product_page = products_page.get_product_price()
    products_page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.correctly_product_name_in_cart(name_in_product_page)
    cart_page.correctly_product_price_in_cart(price_in_product_page)
