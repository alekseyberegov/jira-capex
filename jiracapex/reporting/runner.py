import pandas as pd
from typing import Dict
from jiracapex.utils.template import render_template
from jiracapex.reporting.context import ReportContext

class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def get_report(self, name: str, context: ReportContext):
        mod = __import__(f"jiracapex.reporting.catalog.{name}", None, None, ["init_report"])
        return mod.init_report(context)

    def run_report(self, name: str, context: ReportContext):
        # load the report with the given name
        rep = self.get_report(name, context)
        # read sql query
        with open(rep['query'], 'r') as reader:
            query = reader.read()
        # prepare sql by replacing macros with arguments
        sql = context.prepare_sql(query)
        # run sql and load results in the dataframe
        self.___df = pd.read_sql(sql, con=self.__engine) 

    def run_query(self, sql: str, params: Dict):
        prepared_sql = render_template(sql, params)
        self.___df = pd.read_sql(
            prepared_sql,
            con=self.__engine
        )
        
    @property
    def df(self):
        return self.___df
