from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Date(object):

    def __init__(self, year_month):
        self.__year_month = year_month

    def date_range(self):
        return range((self.__get_end() - self.__get_start()).days + 1)

    def get_date_text(self, n):
        return (self.__get_start() + timedelta(n)).strftime('%Y/%m/%d')

    def __get_start(self):
        return datetime.strptime(self.__year_month + '01', '%Y%m%d')

    def __get_end(self):
        return self.__get_start() + relativedelta(months=1, days=-1)
