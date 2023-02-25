import datetime
td = datetime.date.today()
tm = td + datetime.timedelta(days=1)
yd = td - datetime.timedelta(days=1)
print(yd)
print(td)
print(tm)