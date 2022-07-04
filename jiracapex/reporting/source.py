from pandas import DataFrame
from abc import ABC, abstractmethod
import pandas as pd
from typing import Any
from jiracapex.reporting.context import ReportContext

class ReportSource(ABC):
    abstractmethod
    def configure(self, uri: str, context: ReportContext, **kwargs) -> None:
        pass

    @abstractmethod
    def extract(self, driver: Any) -> DataFrame:
        pass

class DmbsSource(ReportSource):
    def configure(self, uri: str, context: ReportContext, **kwargs) -> None:
        with open(uri, 'r') as inp: sql = inp.read()
        self.__sql = context.replace_str(sql)

    def extract(self, driver: Any) -> DataFrame:
        return pd.read_sql(self.__sql, con=driver) 

class FileSource(ReportSource):
    def configure(self, uri: str, context: ReportContext, **kwargs) -> None:
        self.__file = uri

    def extract(self, driver: Any) -> DataFrame:
        pass

class NullSource(ReportSource):
    def configure(self, uri: str, context: ReportContext, **kwargs) -> None:
        pass

    def extract(self, driver: Any) -> DataFrame:
        pass