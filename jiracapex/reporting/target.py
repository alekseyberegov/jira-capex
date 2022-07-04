from pandas import DataFrame
from abc import ABC, abstractmethod
from typing import Any

class ReportTarget(ABC):
    abstractmethod
    def configure(self, output, **kwargs) -> None:
        pass

    @abstractmethod
    def save(self, driver: Any, df: DataFrame) -> None:
        pass

class DbmsTarget(ReportTarget):
    def configure(self, output, **kwargs) -> None:
        self.__output = output
        self.__params = dict(kwargs)

    def save(self, driver: Any, df: DataFrame) -> None:
        df.to_sql(name=self.__output, con=driver, if_exists='replace')

class FileTarget(ReportTarget):
    def configure(self, output, **kwargs) -> None:
        pass

    def save(self, driver: Any, df: DataFrame) -> None:
        pass

class NullTarget(ReportTarget):
    def configure(self, output, **kwargs) -> None:
        pass

    def save(self, driver: Any, df: DataFrame) -> None:
        pass
