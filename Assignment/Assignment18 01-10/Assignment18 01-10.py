import datetime

td=datetime.datetime.today()
print(td)
yes=datetime.timedelta(days=1)
print(td-yes)
tom=datetime.timedelta(days=-1)
print(td-tom)