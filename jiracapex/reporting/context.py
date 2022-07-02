from typing import Any, Dict
from jiracapex.utils.template import render_template

class ReportContext:
    def __init__(self) -> None:
        self.__variables: Dict[str,str] = {}

    def __getitem__(self, key):
        return self.__variables[key]

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
