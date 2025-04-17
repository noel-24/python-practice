# -*- coding: utf-8 -*-
"""calendar

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bMnNJhNl_u42ge681LN-qpfSlQnLo6Ot
"""

import calendar, datetime

#今日の年月を取得
def getDate():
  M =datetime.date.today().month
  Y =datetime.date.today().year
  return Y, M

#テキストファイルに書き出し
def createFile(thismonth_calendar, filename='test_calendar.txt'):
  with open(filename, mode='w') as f:
    print(thismonth_calendar, file=f)
  print("text書き出し完了")

# ここから本編
Y, M = getDate()
thismonth_calendar = calendar.month(Y, M, w=2, l=1)
print(thismonth_calendar)
createFile(thismonth_calendar)

import datetime
# 日付
today = datetime.date.today()
print(today)
M =today.month
print(M)
Y =datetime.date.today().year
print(Y)

#日時
dt = datetime.datetime.now()
print(dt)
print(dt.strftime('%Y年%m月%d日 %H時%M分%S秒'))