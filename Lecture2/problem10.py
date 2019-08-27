import datetime,time
dt=datetime.date.today()
deltaday5=datetime.timedelta(days=5)
deltasec5=datetime.timedelta(seconds=5)

dtime=datetime.datetime.today()

print("Curent year is:",dt.year)
print("Curent Month is:",dt.month)

print("Curent weekday is:",dtime.isoweekday())
print("Curent year and time is:",dtime.year,dtime.time())
print("Curent time minus 5 days :",dtime-deltaday5)
print("Curent time plus 5 second :",dtime+deltasec5)

      
     
      


