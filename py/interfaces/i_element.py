from selenium.webdriver.remote.webdriver import WebElement

from abc import abstractmethod


class IElement(object):

    @abstractmethod
    def not_exist(self) -> bool:
        pass

    @abstractmethod
    def is_displayed(self) -> bool:
        pass

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def webelement(self) -> WebElement:
        pass
