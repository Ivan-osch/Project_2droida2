from abc import abstractmethod


class IPage(object):

    @abstractmethod
    def is_navigated(self) -> bool:
        pass

    @abstractmethod
    def is_opened(self) -> bool:
        pass
