import importlib
from typing import Dict
from jiracapex.json.utils import flatten_json
from datetime import datetime
from sqlalchemy import Table, Column, MetaData, Integer, String, Date

class DynaObject:
    date_format: str = "%Y-%m-%dT%H:%M:%S.%fZ"

    def __init__(self, name: str) -> None:
        self.__mapping = importlib.import_module('jiracapex.orm.mapping.' + name)
        self.__fields = getattr(self.__mapping, 'fields_map')
        self.__table = None

    @property
    def table_name(self) -> str:
        return getattr(self.__mapping, 'table')

    @property
    def primary_key(self) -> str:
        return getattr(self.__mapping, 'primary_key')

    @property
    def foreign_keys(self) -> str:
        return getattr(self.__mapping, 'foreign_keys')

    @property
    def date_fields(self) -> str:
        return getattr(self.__mapping, 'date_fields')

    @staticmethod
    def to_date(value: str) -> datetime:
        return datetime.strptime(value, DynaObject.date_format)

    def get_field(self, name: str) -> str:
        return self.__fields[name]

    def map_object(self, obj: Dict) -> Dict:
        out = {}
        flattend: Dict = flatten_json(obj)
        for key, value in flattend.items():
            if key in self.__fields:
                out[self.__fields[key]] = value
        
        return out

    def make_table(self, metadata: MetaData) -> Table:
        if self.__table is None:
            cols = []
            for name in self.__fields.values():
                if name == self.primary_key:
                    cols.append(Column(name, Integer, primary_key=True))
                elif name in self.foreign_keys:
                    cols.append(Column(name, Integer))
                elif name in self.date_fields:
                    cols.append(Column(name, Date))
                else:
                    cols.append(Column(name, String(120)))
            self.__table = Table(self.table_name, metadata, *cols)
        return self.__table
