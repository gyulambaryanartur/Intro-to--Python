import datetime,time,calendar
birthdate=datetime.date(1985,1,21)
print("My birthday is:",birthdate)
print("My birthday year is:",birthdate.year)
print("My birthday month is:",birthdate.month)
print("My birthday day is:",birthdate.day)
print("My birthday week is:",birthdate.weekday())
next_birthday=datetime.date(2020,1,21)
today=datetime.date.today()
birthdaycount=next_birthday-today
print("birth days remains:",birthdaycount)
cmaycalendar=calendar.month(2017,5)
print("Calendar of : \n %s "%cmaycalendar)
yesterdaydelta=datetime.timedelta(days=1)
yesterday=today-yesterdaydelta
print("Yesterday date is:",yesterday,"Now is : %s time"%datetime.datetime.today().time())
print("Yesterday  add 2 day date is:",yesterday+datetime.timedelta(days=2))
print("Yesterday subtarct 3 day date is:",yesterday-datetime.timedelta(days=3))

