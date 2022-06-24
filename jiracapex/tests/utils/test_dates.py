import datetime
from typing import List
from jiracapex.utils.dates import last_day_of_month, list_months

def __d(s: str) -> datetime.date:
    return datetime.date.fromisoformat(s)

def test_list_months_the_same_date() -> None:
    beg_date: datetime.date = __d('2022-06-24')
    end_date: datetime.date = __d('2022-06-24')

    months: List = list_months(beg_date, end_date)
    assert len(months) == 1
    assert months[0][0] == beg_date
    assert months[0][1] == end_date

def test_list_months_next_year() -> None:
    beg_date: datetime.date = __d('2022-12-24')
    end_date: datetime.date = __d('2023-01-10')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 2
    assert months[0][0] == beg_date
    assert months[0][1] == __d('2022-12-31')
    assert months[1][0] == __d('2023-01-01')
    assert months[1][1] == end_date

def test_list_months_end_year() -> None:
    beg_date: datetime.date = __d('2022-12-24')
    end_date: datetime.date = __d('2022-12-31')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 1
    assert months[0][0] == beg_date
    assert months[0][1] == __d('2022-12-31')

def test_list_months_the_same_month() -> None:
    beg_date: datetime.date = __d('2022-05-24')
    end_date: datetime.date = __d('2022-05-27')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 1
    assert months[0][0] == beg_date
    assert months[0][1] == end_date

def test_list_months_many_months() -> None:
    beg_date: datetime.date = __d('2022-02-24')
    end_date: datetime.date = __d('2022-05-27')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 4
    assert months[0][0] == beg_date
    assert months[0][1] ==  __d('2022-02-28')
    assert months[1][0] ==  __d('2022-03-01')
    assert months[1][1] ==  __d('2022-03-31')
    assert months[2][0] ==  __d('2022-04-01')
    assert months[2][1] ==  __d('2022-04-30')
    assert months[3][0] ==  __d('2022-05-01')
    assert months[3][1] == end_date

def test_list_months_end_of_month() -> None:
    beg_date: datetime.date = __d('2022-02-24')
    end_date: datetime.date = __d('2022-02-28')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 1
    assert months[0][0] == beg_date
    assert months[0][1] == end_date

def test_list_months_end_of_month_next_month() -> None:
    beg_date: datetime.date = __d('2022-02-24')
    end_date: datetime.date = __d('2022-03-31')
    months: List = list_months(beg_date, end_date)
    assert len(months) == 2
    assert months[0][0] == beg_date
    assert months[0][1] ==  __d('2022-02-28')
    assert months[1][0] ==  __d('2022-03-01')
    assert months[1][1] == end_date
  





