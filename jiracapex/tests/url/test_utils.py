import pytest
from jiracapex.url.utils import url_add_params

def test_set_params():
    url = 'http://www.domain.com'
    assert url_add_params(url, {'a': 1, 'b': 2}) == url + '?a=1&b=2'

def test_add_params():
    url = 'http://www.domain.com?c=0'
    assert url_add_params(url, {'a': 1, 'b': 2}) == url + '&a=1&b=2'