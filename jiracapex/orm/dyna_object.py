import importlib
from typing import Dict
from jiracapex.json.utils import flatten_json
from datetime import datetime
from sqlalchemy import Table, Column, MetaData, Integer, String, Date
from sqlalchemy import create_engine, insert

class DynaObject:
    date_format: str = "%Y-%m-%dT%H:%M:%S.%fZ"

    def __init__(self, name: str) -> None:
        self.__mapping = importlib.import_module('jiracapex.orm.mapping.' + name)
        self.__fields  = getattr(self.__mapping, 'fields_map')
        self.__table   = None
        self.__engine  = None
        self.__queue   = []

    @property
    def table_name(self) -> str:
        return getattr(self.__mapping, 'table')

    @property
    def table(self) -> Table:
        return self.__table

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

    def cast(self, obj: Dict) -> Dict:
        out = {}
        for key, value in flatten_json(obj).items():
            if key in self.__fields:
                col_name: str = self.__fields[key] 

                if col_name == self.primary_key or col_name in self.foreign_keys:
                    col_value = int(value)
                elif col_name in self.date_fields:
                    col_value = self.to_date(value)
                else:
                    col_value = value

                out[col_name] = col_value
        
        return out

    def storage(self, metadata: MetaData) -> Table:
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

    def create_table(self, checkfirst = True) -> Table:
        """
            Creates a table to store objects for this mappinng

            Parameters
            ----------
            checkfirst: bool
                indicates whether to check existence of the table first

            Returns
            -------
            Table
        """
        table: Table = self.storage(MetaData())
        table.create(self.__engine, checkfirst=checkfirst)
        return table

    def bind(self, engine) -> 'DynaObject':
        self.__engine = engine
        return self

    def insert(self, obj: Dict) -> None:
        with self.__engine.connect() as conn:
            tran = conn.begin()
            conn.execute(insert(self.__table), [self.cast(obj)])
            tran.commit()

    def add(self, obj: Dict) -> None:
        self.__queue.append(self.cast(obj))

    def flush(self) -> None:
        if len(self.__queue) > 0:
            with self.__engine.connect() as conn:
                tran = conn.begin()
                for o in self.__queue:
                    conn.execute(insert(self.__table), [o])
                tran.commit()
                self.__queue.clear()
