from pandas import DataFrame
from abc import ABC, abstractmethod
from typing import Any

class ReportSource(ABC):
    abstractmethod
    def configure(self, output, **kwargs) -> None:
        pass

    @abstractmethod
    def load(self, driver: Any) -> DataFrame:
        pass