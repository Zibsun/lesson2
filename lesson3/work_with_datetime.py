from datetime import datetime, timedelta

today = datetime.now()
print ("Today is " + today.strftime("%d%/%m/%Y"))
print ("Yesterday was " + (today-timedelta(days = 1)).strftime("%d%/%m/%Y"))
the_year = today.year
the_month = today.month
if the_month == 1:
    dt1 = today.replace(month = 12, year = the_year - 1)
else:
    dt1 = today.replace(month = the_month - 1)
print ("Last month is " + dt1.strftime("%d%/%m/%Y"))


s = "12/1/17 12:10:03.234567"
print(datetime.strptime(s, "%d/%m/%y %H:%M:%S.%f"))