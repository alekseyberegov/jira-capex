import pandas as pd
from typing import Dict
from jiracapex.utils.template import render_template

class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def run(self, sql: str, params: Dict):
        prepared_sql = render_template(sql, params)
        self.___df = pd.read_sql(
            prepared_sql,
            con=self.__engine
        )
        
    @property
    def df(self):
        return self.___df