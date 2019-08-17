from bs4 import BeautifulSoup

from dailyLearningReportScraping.account import Account


class DailyReport(object):

    def __init__(self, session):
        self.__session = session

    def login(self):
        res = self.__session.post("https://member.toraiz.jp/toraiz/auth/login", data=Account().get_login_info())
        res.raise_for_status()

    def get(self, date):
        return self.__parse_text(self.__get_data_from_site(date))

    def __get_data_from_site(self, date):
        res = self.__session.get("https://member.toraiz.jp/toraiz/report?date=" + date)
        res.raise_for_status()
        return res.text

    def __parse_text(self, daily_report_text):
        soup = BeautifulSoup(daily_report_text, 'html.parser')

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

    @staticmethod
    def __get_from_element(soup, element):
        element_value = soup.select(element)
        return element_value[0]["value"] if element_value else "0"

    @staticmethod
    def __format_time(hour, minutes):
        return hour.zfill(2) + ":" + minutes.zfill(2)
