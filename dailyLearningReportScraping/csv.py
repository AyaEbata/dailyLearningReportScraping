import csv
import os


class Csv(object):

    def __init__(self, year_month):
        self.__year_month = year_month

    def write_header_to_csv(self):
        os.makedirs(self.__directory_name(), exist_ok=True)

        with open(self.__file_name(), 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([["日付", "リスニング勉強時間", "スピーキング勉強時間", "レッスン時間", "レッスン予習、その他の勉強時間"]])

    def write_data_to_csv(self, daily_report_element):
        with open(self.__file_name(), 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([list(daily_report_element)])

    @staticmethod
    def __directory_name():
        return 'DailyLearningReport'

    def __file_name(self):
        return self.__directory_name() + '/' + self.__year_month + '.csv'
