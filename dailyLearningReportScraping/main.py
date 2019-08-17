import csv
import os
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

from dailyLearningReportScraping.account import Account


class Main(object):

    def __init__(self, year_month):
        self.__session = self.__start_session()
        self.__year_month = year_month
        self.__directory_name = 'DailyLearningReport'
        self.__file_name = self.__directory_name + '/' + self.__year_month + '.csv'

    def scraping(self):
        self.__login()

        self.__write_header_to_csv()

        start = datetime.strptime(self.__year_month + '01', '%Y%m%d')
        end = start + relativedelta(months=1, days=-1)

        for n in range((end - start).days + 1):
            date = start + timedelta(n)

            daily_report = self.__get_daily_report(date.strftime('%Y/%m/%d'))
            daily_report_element = self.__parse_daily_report(daily_report)
            self.__write_data_to_csv(daily_report_element)

    @staticmethod
    def __start_session():
        return requests.session()

    def __login(self):
        res = self.__session.post("https://member.toraiz.jp/toraiz/auth/login", data=Account().get_login_info())
        res.raise_for_status()

    def __get_daily_report(self, date):
        res = self.__session.get("https://member.toraiz.jp/toraiz/report?date=" + date)
        res.raise_for_status()
        return res.text

    def __parse_daily_report(self, daily_report):
        soup = BeautifulSoup(daily_report, 'html.parser')

        date = soup.find("input", id="date")["value"]
        listening_hour = self.__get_from_element(soup, "select#hour_l>option:checked")
        listening_minutes = self.__get_from_element(soup, "select#minute_l>option:checked")
        speaking_hour = self.__get_from_element(soup, "select#hour_s>option:checked")
        speaking_minutes = self.__get_from_element(soup, "select#minute_s>option:checked")
        lesson_hour = self.__get_from_element(soup, "select#hour_le>option:checked")
        lesson_minutes = self.__get_from_element(soup, "select#minute_le>option:checked")
        other_hour = self.__get_from_element(soup, "select#hour_o>option:checked")
        other_minutes = self.__get_from_element(soup, "select#minute_o>option:checked")

        return date, self.__format_time(listening_hour, listening_minutes), self.__format_time(speaking_hour, speaking_minutes), self.__format_time(lesson_hour, lesson_minutes), self.__format_time(other_hour, other_minutes)

    def __write_header_to_csv(self):
        os.makedirs(self.__directory_name, exist_ok=True)

        with open(self.__file_name, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([["日付", "リスニング勉強時間", "スピーキング勉強時間", "レッスン時間", "レッスン予習、その他の勉強時間"]])

    def __write_data_to_csv(self, daily_report_element):
        with open(self.__file_name, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([list(daily_report_element)])

    @staticmethod
    def __get_from_element(soup, element):
        element_value = soup.select(element)
        return element_value[0]["value"] if element_value else "0"

    @staticmethod
    def __format_time(hour, minutes):
        return hour.zfill(2) + ":" + minutes.zfill(2)
