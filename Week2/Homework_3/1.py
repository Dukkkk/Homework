import datetime as dt
date = "2024/12/15"
datetime = dt.datetime.strptime(date, "%Y/%m/%d")
print(datetime)