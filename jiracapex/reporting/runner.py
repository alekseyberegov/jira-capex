import pandas as pd
from pandas import DataFrame
from typing import Dict, Any
from jiracapex.utils.template import render_template
from jiracapex.reporting.context import ReportContext
from jiracapex.reporting.target import DbmsTarget, FileTarget, NullTarget, ReportTarget
from jiracapex.reporting.source import DmbsSource, DmbsSource, ReportSource

class Report:
    __NULL_TARGET: Dict = {'type': None, 'output': None, 'options': {}}
    __NULL_SOURCE: Dict = {'type': None,  'input': None, 'options': {}}

    __TARGET_FACTORY = {
        'dbms': DbmsTarget,
        'file': FileTarget,
         None : NullTarget
    }

    __SOURCE_FACTORY = {
        'dbms': DmbsSource,
         None : DmbsSource
    }

    @classmethod
    def new_instance(cls, name: str, context: ReportContext) -> 'Report':
        mod = __import__(f"jiracapex.reporting.catalog.{name}", None, None, ["init_report"])
        return Report(mod.__init__(context), context)
    
    def __init__(self, config: Dict, context: ReportContext) -> None:
        self.__config  = config
        self.__context = context

    def make_target(self, key: str, output: str, **kwargs) -> ReportTarget:
        target: ReportTarget = Report.__TARGET_FACTORY[key]()
        target.configure(output, **kwargs)
        return target

    def make_source(self, key: str, input: str, **kwargs) -> ReportSource:
        source: ReportSource = Report.__SOURCE_FACTORY[key]()
        source.configure(input, self.__context, **kwargs)
        return source 

    def __getitem__(self, key):
        return self.__config[key]

    def __contains__(self, key):
        return key in self.__config

    def transform(self, df: DataFrame) -> DataFrame:
        for m in [self.derive, self.select, self.split, self.colsort, self.index]:
            df = m(df)
        return df

    def derive(self, df: DataFrame) -> DataFrame:
        if 'derive' in self:
            for m in self['derive']:
                df[m['name']] = m['calc'](df)
        return df

    def select(self, df: DataFrame) -> DataFrame:
        if 'schema' in self:
            df = df[self['schema'].keys()]
        return df

    def split(self, df: DataFrame) -> DataFrame:
        if 'split' in self:
            for col in self['split']:
                df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series)], axis=1)
        return df

    def index(self, df: DataFrame) -> DataFrame:
        if 'index' in self:
           df =  df.set_index(self['index'])
        return df

    def colsort(self, df: DataFrame) -> DataFrame:
        return df.reindex(sorted(df.columns), axis=1)

    @property
    def target(self) -> ReportTarget:
        params: Dict = self.__config.get('target', Report.__NULL_TARGET)
        return self.make_target(params['type'], params['output'], **params['options'])

    @property
    def source(self) -> ReportSource:
        params: Dict = self.__config.get('source', Report.__NULL_SOURCE)
        return self.make_source(params['type'], params['input'], **params['options'])     

class ReportRunner:
    def __init__(self, engine) -> None:
        self.__engine = engine

    def run(self, report: Report) -> DataFrame:
        df = report.transform(report.source.extract(self.__engine))
        report.target.save(self.__engine, df)
        return df

    def query(self, sql: str, params: Dict) -> DataFrame:
        return pd.read_sql(render_template(sql, params), con=self.__engine)
