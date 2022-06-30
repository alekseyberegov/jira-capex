from typing import Any, Dict
from jiracapex.utils.template import render_template

class ReportContext:
    def __init__(self) -> None:
        self.__variables: Dict[str,str] = {}
        self.__arguments: Dict[str,Any] = {}

    def set_var(self, name: str, value: str) -> None:
        self.__variables[name] = value

    def set_arg(self, name: str, value: Any) -> None:
        self.__arguments[name] = value

    def prepare_sql(self, sql: str) -> str:
       return render_template(sql, self.__arguments)

    def process(self, report: Dict) -> Dict:
        return self.replace_vars(dict(report))

    def replace_vars(self, o: Any) -> Dict:
        if type(o) is str:
            return render_template(o, self.__variables)

        if type(o) is dict:
            for n,v in o.items():
                o[n] = self.replace_vars(v)
            return o

        if type(o) is list:
            l = []
            for v in o:
                l.append(self.replace_vars(v))
            return l

        return o
