import pandas as pd
from typing import Dict
from jiracapex.utils.template import render_template

class ReportContext:
    def __init__(self) -> None:
        pass


def load_report(name: str, context: ReportContext):
    mod = __import__(f"jiracapex.reporting.catalog.{name}", None, None, ["init_report"])
    return mod.init_report(context)


class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def run_report(self, name: str, context: ReportContext):
        rep: Dict = load_report(name, context) 

    def run_query(self, sql: str, params: Dict):
        prepared_sql = render_template(sql, params)
        self.___df = pd.read_sql(
            prepared_sql,
            con=self.__engine
        )
        
    @property
    def df(self):
        return self.___df

