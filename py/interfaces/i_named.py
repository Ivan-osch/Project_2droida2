class INamed:

    _name = None

    def set_name(self, name: str):
        self._name = name
        return self

    def get_name(self) -> str:
        return self._name
