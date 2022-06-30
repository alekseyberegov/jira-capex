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

    def replace_vars(self, o: Dict) -> Dict:
        for n,v in o.items():
            if type(v) is str:
                o[n] = render_template(v, self.__variables)
            elif type(v) is dict:
                self.replace_vars(v)
            elif type(v) is list:
                l = []
                for i in v:
                    l.append(render_template(i, self.__variables))
                o[n] = l
        return o
