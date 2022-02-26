from urllib.parse import urlparse, parse_qsl, urlencode, ParseResult
from typing import Dict

def url_add_params(url: str, params: Dict[str,str]):
    parsed = urlparse(url)
    url_dict = dict(parse_qsl(parsed.query))
    url_dict.update(params)
    qs = urlencode([(k, v) for k, v in url_dict.items() if v is not None])
    new = ParseResult(
        parsed.scheme, 
        parsed.netloc,
        parsed.path, 
        parsed.params,
        qs, 
        parsed.fragment)

    return new.geturl()