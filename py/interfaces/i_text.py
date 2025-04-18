from abc import abstractmethod


class IText:

    @abstractmethod
    def text(self) -> str:
        pass
