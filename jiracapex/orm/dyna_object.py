from pathlib import Path
import importlib

class DynaObject:
    def __init__(self, name: str) -> None:
        mod = importlib.import_module('jiracapex.orm.mapping.' + name)
        self.__fields = getattr(mod, 'fields_map')

    def get_field(self, name: str) -> str:
        return self.__fields[name]


