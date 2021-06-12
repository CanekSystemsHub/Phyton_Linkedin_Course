#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  
  #### Date Formatting ####
  now = datetime.now()
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current Year is %Y"))
  print(now.strftime("%a, %d, %B, %Y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Locale date and time %c"))
  print(now.strftime("Locale date %X"))
  print(now.strftime("Locale time %x"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Formatted Current Time is: %I:%M:%S %p"))
  print(now.strftime("Locale 24H time is: %H:%M"))

if __name__ == "__main__":
  main();
