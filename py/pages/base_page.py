from selenium.webdriver.common.by import By

from py.interfaces.i_named import INamed
from py.interfaces.i_page import IPage
from py.htmlelements.htmlelement import HtmlElement
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage(IPage, INamed):

    by = selector = None
    driver = None
    _url = ""

    is_opened_element = HtmlElement(By.CSS_SELECTOR, "body", "элемент проверки открытия страницы")
    #popup_confirmation = ConfirmationDialog()
    #message = MessagePopup()

    def __str__(self):
        try:
            return f"Страница {self.get_name()}"
        except AttributeError:
            return self.__class__.__name__

    def __init__(self, driver: WebDriver = None):
        self._base_url: str = ""
        if driver:
            if not isinstance(driver, WebDriver):
                raise TypeError('В класс страницы передан не драйвер, а %s' % type(driver))
            self.driver: WebDriver = driver
            #self.config: Config = Config()
            self._base_url = self.config.get("BASE_URL", "GENERAL")
            # self.browser: Browser = Browser(driver)
            self.init()

    def get_elements(self) -> tuple:
        """Получение потенциально элементов из класса
         нужен из-за того что dir вычисляет свойства, а нам нужны только атрибуты класса"""

        for _class in self.__class__.__mro__:
            for key, value in _class.__dict__.items():
                if not key.startswith('_') and not isinstance(getattr(self.__class__, key), property):
                    value = getattr(self, key)
                    if isinstance(value, (HtmlElement, BasePage)):
                        yield key, value

    def init(self):
        """Инициализация класса когда передали driver"""

        for key, cur_value in self.get_elements():
            if isinstance(cur_value, HtmlElement):
                try:
                    setattr(self, key, cur_value.new_instance(driver=self.driver, page=self, name=key))
                except Exception as error:
                    raise type(error)(f'Не смогли создать копию элемента\n'
                                      f'key: {key}\n'
                                      f'type: {type(cur_value)}\n'
                                      f'{repr(error)}')
            elif isinstance(cur_value, BasePage):
                cur_value.__init__(self.driver)

    def get_page_url(self) -> str:
        return self._base_url.strip('/') + '/' + self._url.strip('/')

    def navigate_to(self):
        self.driver.get(self.get_page_url())

    def open_page(self, url):
        """Открыть страницу"""
        self.driver.get(url)















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
