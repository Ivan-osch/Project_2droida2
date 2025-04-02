from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductPage(BasePage):
    def sort_by_increase(self):
        self.browser.find_element(*ProductsPageLocators.SORT_BY_PRODUCT).click()
        self.browser.find_element(*ProductsPageLocators.SORT_BY_INCREASE).click()

    def sort_by_decrease(self):
        self.browser.find_element(*ProductsPageLocators.SORT_BY_PRODUCT).click()
        self.browser.find_element(*ProductsPageLocators.SORT_BY_DECREASE).click()

    def should_be_sort_by_increase(self):
        prices = self.browser.find_elements(*ProductsPageLocators.PRICE_PRODUCTS_IN_PAGE)
        price_min = float(prices[0].text)
        for price in prices:
            assert float(price.text) >= price_min, "Сортировка по возрастанию некорректна"
            price_min = float(price.text)

    def should_be_sort_by_decrease(self):
        prices = self.browser.find_elements(*ProductsPageLocators.PRICE_PRODUCTS_IN_PAGE)
        price_max = float(prices[0].text)
        for price in prices:
            assert float(price.text) <= price_max, "Сортировка по убыванию некорректна"
            price_max = float(price.text)