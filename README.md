# 某英語教室の学習報告ページから報告済みのデータを取得するヤツ〜見事に雑なスクレイピング〜

## 準備
- venvでactivateする。
- config/account_sample.ymlをコピーしてconfig/account.ymlを作成し、アカウント情報を入力する。

## 実行方法
第一引数に取得したい年月を指定する。
（run library module as a scriptやから、-mやで）

```bash
# python -m dailyLearningReportScraping [year_month]
$ python -m dailyLearningReportScraping 201908
```

## メモ
### venv
使うとき（作業するディレクトリに入ってから）
```bash
$ source ./bin/activate
```

抜け出すとき
```bash
$ Deactivate
```