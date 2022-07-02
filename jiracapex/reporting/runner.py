import pandas as pd
from pandas import DataFrame
from abc import ABC, abstractmethod
from typing import Dict
from jiracapex.utils.template import render_template
from jiracapex.reporting.context import ReportContext

class ReportTarget(ABC):
    @abstractmethod
    def save(self, df: DataFrame, output, engine, **kwargs) -> None:
        pass

class DbmsTarget(ReportTarget):
    def save(self, df: DataFrame, output, engine, **kwargs) -> None:
        df.to_sql(name=output, con=engine, if_exists='replace')

class FileTarget(ReportTarget):
    def save(self, df: DataFrame, output, engine, **kwargs) -> None:
        pass

class NullTarget(ReportTarget):
    def save(self, df: DataFrame, output, engine, **kwargs) -> None:
        pass

REPORT_TARGETS = {
    'dbms': DbmsTarget(),
    'file': FileTarget(),
    'null': NullTarget()
}

class Report:
    def __init__(self, config: Dict) -> None:
        self.__config = config

    def __getitem__(self, key):
        return self.__config[key]

    def __contains__(self, key):
        return key in self.__config

    def sql(self, context: ReportContext) -> str:
        with open(self['query'], 'r') as inp: sql = inp.read()
        return context.replace_str(sql)

    def derive(self, df: DataFrame) -> DataFrame:
        if 'derive' in self:
            for m in self['derive']:
                df[m['name']] = m['calc'](df)
        return df

    def select(self, df: DataFrame) -> DataFrame:
        return df[self['schema'].keys()]

    def split(self, df: DataFrame) -> DataFrame:
        if 'split' in self:
            for col in self['split']:
                df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series)], axis=1)
        return df

    def save(self, df: DataFrame, engine):
        if 'target' in self:
            params: Dict = self['target']
            target: ReportTarget = REPORT_TARGETS.get(params['type'])
            target.save(df, params['output'], engine, **params['options'])

class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def get_report(self, name: str, context: ReportContext) -> Report:
        mod = __import__(f"jiracapex.reporting.catalog.{name}", None, None, ["init_report"])
        return Report(mod.__init__(context))

    def run_report(self, name: str, context: ReportContext):
        rpt: Report = self.get_report(name, context)
        # run report SQL
        df = pd.read_sql(rpt.sql(context), con=self.__engine) 
        # calculate derived values
        df = rpt.derive(df)
        # subselect columns
        df = rpt.select(df)
        # split columns
        df = rpt.split(df)
        # sort columns
        df = df.reindex(sorted(df.columns), axis=1)
        # generate output
        rpt.save(df, self.__engine)
        # keep dataframe
        self.__df = df

    def run_query(self, sql: str, params: Dict):
        prepared_sql = render_template(sql, params)
        self.__df = pd.read_sql(
            prepared_sql,
            con=self.__engine
        )
        
    @property
    def df(self):
        return self.__df
