import pandas as pd
from pandas import DataFrame
from abc import ABC, abstractmethod
from typing import Dict, Any
from jiracapex.utils.template import render_template
from jiracapex.reporting.context import ReportContext

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


class Report:
    __NULL_TARGET: Dict = {'type': None, 'output': None, 'options': {}}

    __TARGET_FACTORY = {
        'dbms': DbmsTarget,
        'file': FileTarget,
         None : NullTarget
    }

    @classmethod
    def make_target(cls, key: str) -> ReportTarget:
        return Report.__TARGET_FACTORY[key]()
    
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

    def colsort(self, df: DataFrame) -> DataFrame:
        return df.reindex(sorted(df.columns), axis=1)

    def target(self) -> ReportTarget:
        cfg: Dict = self.__config.get('target', Report.__NULL_TARGET)
        tgt: ReportTarget = Report.make_target(cfg['type'])
        tgt.configure(cfg['output'], **cfg['options'])
        return tgt

class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def get_report(self, name: str, context: ReportContext) -> Report:
        mod = __import__(f"jiracapex.reporting.catalog.{name}", None, None, ["init_report"])
        return Report(mod.__init__(context))

    def run_report(self, name: str, context: ReportContext):
        rp: Report = self.get_report(name, context)
        # run report SQL
        df = pd.read_sql(rp.sql(context), con=self.__engine) 
        # process the report
        for m in [rp.derive, rp.select, rp.split, rp.colsort]:
            df = m(df)
        # save report
        rp.target().save(self.__engine, df)
        # keep the dataframe
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
