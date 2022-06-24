import datetime
from typing import List

def last_day_of_month(any_day: datetime) -> datetime:
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month,
    #  or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

def list_months(beg_date: datetime.date, end_date: datetime.date) -> List:
    months = []
    cur_date: datetime.date = beg_date
    while True:
        next_month = cur_date.replace(
                year=cur_date.year + (cur_date.month + 1) // 12,
                month=(cur_date.month % 12) + 1, 
                day=1)
        if next_month > end_date:
            break
        months.append([cur_date, last_day_of_month(cur_date)])
        cur_date = next_month

    months.append([cur_date, end_date])
    return months

