import calendar
import datetime


def sum_days_in_month():
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    return days_in_month
