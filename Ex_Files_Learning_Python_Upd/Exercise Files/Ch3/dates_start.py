#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print ("today's day is ", today)

  # print out the date's individual components
  print("Print date individual components", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's week day number is ", today.weekday())
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  print("Which is the day ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today1 = datetime.now()
  print("DATETIME Notation - Today is ", today1)
  
  # Get the current time
  time = datetime.time(datetime.now())
  print("And the current time is: ", time)

 

  
if __name__ == "__main__":
  main();
  