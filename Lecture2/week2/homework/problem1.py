import datetime,time
import argparse
dy_years=365.25

deltaday=datetime.timedelta(days=0)
parser =argparse.ArgumentParser()
parser.add_argument("num_y",help="Dispay count of years",type=int)
parser.add_argument("--num_d",help="Dispay count of days",type=int)
argument=parser.parse_args()
year=argument.num_y
day= argument.num_d
dt=datetime.datetime.today()
if year:
 deltayear=datetime.timedelta(days=year*dy_years)
 print("Given years:",year)
if day: 
 deltaday=datetime.timedelta(days=day)
 print("Given days:",day)
else:
    print("Given days: not given") 
print("Current date:",dt)
print("Final date:",dt+deltayear+deltaday)


