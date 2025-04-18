#from pages.base_page import BaseElement, BaseView

from .py.pages.base_page import BasePage


def test_should_be_see_sort_in_products_page():
    link = "https://2droida.ru/"
    page = BasePage
    page.open_page(link)
