import sys

from dailyLearningReportScraping.main import Main

if __name__ == "__main__":
    # 実行方法: python -m dailyLearningReportScraping 201908
    Main(sys.argv[1]).scraping()
