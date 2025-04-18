from py.interfaces.i_text import IText
from py.interfaces.i_named import INamed
from py.interfaces.i_element import IElement
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union


class HtmlElement(IElement, INamed, IText):
    """Base element"""

    driver: WebDriver = None
    absolute_position = None

    def __str__(self):
        return self._name

    def __init__(self, by_type: str, selector: Union[str, tuple], name: str = "", **kwargs):
        self._by = by_type
        if by_type is not None:
            self._by_selector = selector
        self.driver: WebDriver = kwargs.get("driver", None)
        self.parent = kwargs.get("parent")
        self.page = kwargs.get("page")
        self._name = name if name else self.__str__()
        self._find_element = None
        self._kwargs = tuple(kwargs.items())
        if kwargs.get("absolute_position"):
            self.absolute_position = kwargs.get("absolute_position")
        if self.driver:
            self.init(self.driver)


    def init(self, driver: WebDriver, parent=None, page=None, name='') -> None:
        """Инициализация элементов"""

        self.driver = driver
        self.parent = self.page = None
        if name:
            self.set_name(name)
        if not self.absolute_position:
            self.page = page

            if not (self.parent and parent is None):
                self.parent = parent
                if parent and page is None:
                    self.page = parent.page

        self.create_child_items()
        if self.absolute_position:
            pass

    def create_child_items(self):
        """Создать дочерние элементы"""

        for key, value in self.get_elements():
            if issubclass(value.__class__, HtmlElement):
                value.init(self.driver, parent=self, page=self.page)

    def new_instance(self, driver, parent=None, page=None, name=''):
        """Получение нового экземпляра элемента"""

        if self._kwargs:
            new_item = type(self)(self._by, self._by_selector, self._name,
                                  **{k: v for k, v in self._kwargs})
        else:
            new_item = type(self)(self._by, self._by_selector, self._name)
        new_item.init(driver, parent=parent or self.parent, page=page)

        return new_item
