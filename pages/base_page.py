from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from conftest import browser
from selenium.webdriver.common.by import By
from .locators import BasePageLocators


class BaseElement:
    def __init__(self, selector: str):
        self.selector = selector
        self._browser: webdriver | None = None

    def bind(self, browser: webdriver) -> 'BaseElement':
        """Создаёт копию элемента, привязанную к конкретному soup"""
        bound = BaseElement(self.selector)
        bound._browser = browser
        return bound

    def get_element(self):
        element = self._browser.find_element(By.CSS_SELECTOR, self.selector)
        return element

    def click(self):
        element = self.get_element()
        element.click()

    def open(self, url):
        self._browser.get(url)

class BaseView:
    def __int__(self, browser):
        self._browser = browser

        """Автоматически связываем все BaseElement поля класса"""
        for attr_name, class_attr in self.__class__.__dict__.items():
            if isinstance(class_attr, BaseElement):
                bound_element = class_attr.bind(self._browser)
                setattr(self, attr_name, bound_element)




    # def button_click_to_be_clickable_and_visibility(self, how, what, timeout=5):
    #     button = WebDriverWait(self.browser, timeout).until(
    #         lambda d: EC.visibility_of_element_located((how, what))(d) and
    #                   EC.element_to_be_clickable((how, what))(d)
    #     )
    #     button.click()
    #
    # def button_click_to_be_visibility(self, how, what, timeout=5):
    #     button = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
    #     button.click()
    #
    # def button_click(self, element, timeout=3):
    #     self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    #     button = WebDriverWait(self.browser, timeout).until(
    #         EC.element_to_be_clickable(element)
    #     )
    #     button.click()
    #
    # def open_catalog(self):
    #     catalog = self.browser.find_element(*BasePageLocators.CATALOG)
    #     catalog.click()
    #
    # def go_to_products_page(self):
    #     elem1 = self.browser.find_element(*BasePageLocators.SMARTFONY)
    #     #  наведение курсора на элемент без нажатия
    #     actions = ActionChains(self.browser)
    #     actions.move_to_element(elem1)
    #     actions.perform()
    #     elem2 = self.browser.find_element(*BasePageLocators.APPLE)
    #     elem2.click()
    #
    # def open(self):
    #     self.browser.get(self.url)
    #
    # def go_to_cart_page(self):
    #     self.button_click_to_be_visibility(*BasePageLocators.BUTTON_CART)
