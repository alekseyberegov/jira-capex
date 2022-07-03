import datetime
from typing import List, Dict

def last_day_of_month(any_day: datetime) -> datetime:
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month,
    #  or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

def list_months(beg_date: datetime.date, end_date: datetime.date) -> List:
    def list_agg(l: List = None, period: List = None) -> list:
        if l is None:
            return []
        l.append(period)
        return l

    return split_into_months(beg_date, end_date, list_agg)

def dict_months(prefix: str, beg_date: datetime.date, end_date: datetime.date) -> Dict:
    def dict_agg(d: Dict = None, period: List = None) -> Dict:
        if d is None:
            return {}
        d[prefix + period[0].strftime('%Y_%m') + '_n'] = (period[1] - period[0]).days + 1
        d[prefix + period[0].strftime('%Y_%m') + '_d'] = ''.join(['[',
            period[0].strftime('%Y-%m-%d'), ',', 
            period[1].strftime('%Y-%m-%d'), ']'
        ])
        return d

    return split_into_months(beg_date, end_date, dict_agg) 

def split_into_months(beg_date: datetime.date, end_date: datetime.date, func):
    months = func()
    cur_date: datetime.date = beg_date
    while True:
        next_month = cur_date.replace(
                year=cur_date.year + (cur_date.month    ) // 12,
                month=(cur_date.month % 12) + 1, 
                day=1)
        if next_month > end_date:
            break
        months = func(months, [cur_date, last_day_of_month(cur_date)])
        cur_date = next_month

    months = func(months, [cur_date, end_date])
    return months
