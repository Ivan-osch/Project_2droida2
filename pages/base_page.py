from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators

import math


class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_catalog(self):
        catalog = self.browser.find_element(*BasePageLocators.CATALOG)
        catalog.click()

    def go_to_products_page(self):
        elem1 = self.browser.find_element(*BasePageLocators.SMARTFONY)
        #  наведение курсора на элемент без нажатия
        actions = ActionChains(self.browser)
        actions.move_to_element(elem1)
        actions.perform()
        elem2 = self.browser.find_element(*BasePageLocators.APPLE)
        elem2.click()

    def open(self):
        self.browser.get(self.url)

    def go_to_cart_page(self):
        button = self.browser.find_element(*BasePageLocators.BUTTON_CART)
        button.click()
