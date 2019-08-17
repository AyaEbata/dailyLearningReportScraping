import requests

from dailyLearningReportScraping.csv import Csv
from dailyLearningReportScraping.daily_report import DailyReport
from dailyLearningReportScraping.date import Date


class Main(object):

    def __init__(self, year_month):
        self.__session = self.__start_session()
        self.__year_month = year_month

    def scraping(self):
        daily_report = DailyReport(self.__session)
        daily_report.login()

        csv = Csv(self.__year_month)
        csv.write_header_to_csv()

        date = Date(self.__year_month)

        for n in date.date_range():
            daily_report_element = daily_report.get(date.get_date_text(n))
            csv.write_data_to_csv(daily_report_element)

    @staticmethod
    def __start_session():
        return requests.session()
