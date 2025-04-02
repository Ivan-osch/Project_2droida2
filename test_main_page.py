from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "https://2droida.ru/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    time.sleep(5)
    page.go_to_basket_page_header()
    time.sleep(5)
