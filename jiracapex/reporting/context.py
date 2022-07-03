import re
from typing import Any, Dict
from jiracapex.utils.template import render_template

def norm(s:str) -> str:
    return re.sub("[^0-9a-zA-Z_]+", "_", s)

class ReportContext:
    def __init__(self) -> None:
        self.__variables: Dict[str,str] = {}

    def __getitem__(self, key):
        fun = None
        if key.startswith('__func_'):
            match = re.search(r"__func_(\w+):(\w+)", key)
            if match:
                fun = globals()[match.group(1)]
                key = match.group(2)

        value = self.__variables[key]
        if fun is not None:
            value = fun(value)
        return value

    def __setitem__(self, key, newvalue):
        self.__variables[key] = newvalue

    def replace_str(self, s: str) -> str:
       return render_template(s, self)

    def replace_obj(self, report: Dict) -> Dict:
        return self.__replace_obj(dict(report))

    def __replace_obj(self, o: Any) -> Dict:
        if type(o) is str:
            return render_template(o, self)

        if type(o) is dict:
            for n,v in o.items():
                o[n] = self.__replace_obj(v)
            return o

        if type(o) is list:
            l = []
            for v in o:
                l.append(self.__replace_obj(v))
            return l

        return o
