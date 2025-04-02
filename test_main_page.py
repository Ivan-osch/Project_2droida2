from .pages.base_page import BasePage
from .pages.products_page import ProductPage
import time


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

