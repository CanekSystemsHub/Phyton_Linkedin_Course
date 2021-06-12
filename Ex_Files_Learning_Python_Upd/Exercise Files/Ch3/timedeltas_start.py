#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is: " + str(now))

# print today's date one year from now
print("one year from now it will be" + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 6 days and 4 weeks it will be the date " + str(now + timedelta(days=6, weeks=4)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago it was the date: " + s)

### How many days until the day I receive my RSU (Yeah!!!1)?
today = date.today()
RSU_Date = date(today.year, 6 ,28)



# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if RSU_Date < today:
    print("RSU already have passed by %d ago" %((today - RSU_Date).days))
    RSU_Date = RSU_Date.replace(year= today.year+1)
else:
    print("RSU day has not went by yet!")

# Now calculate the amount of time until April Fool's Day  
Time_2_RSU = RSU_Date - today
print("It's just ", Time_2_RSU.days, " days for your next RSU distribuition Victor!!!!")
