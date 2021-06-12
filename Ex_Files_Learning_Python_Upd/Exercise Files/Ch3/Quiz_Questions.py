
# 1.- Given that now=datetime.now(), which call may produce different results on different computers?

from datetime import date
from datetime import time
from datetime import datetime 

now = datetime.now()
print("The current date is: ", now)

print(now.strftime("%c"))


# 2.- Which code will you use to generate a date and time output in the following format?
# 13-Mar-2020 16:42:58



# 4.- You create a simple calendar program that needs to print tomorrow's day of the week. Which code will work under all circumstances?

today = date.today()
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be the day : " + days[today.weekday()+1])


otherdatenow = datetime.date(datetime.now())
print(otherdatenow)

