#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  print("Does the Canek's prior TXT File exist? ", str(path.exists("canekfile.txt")))
  print("Does the Canek's prior TXT File is it actually a File??? ", str(path.isfile("canekfile.txt")))
  print("Or such TXT is a directory? ", str(path.isdir("canekfile.txt")))
  # Work with file paths
  print("Where is this TXT file located  ", str(path.realpath("canekfile.txt")))
  print("Split the file's path  ", str(path.split(path.realpath("canekfile.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("canekfile.txt"))
  print("Last change of this file was on: ",t)
  
  # Calculate how long ago the item was modified

  
if __name__ == "__main__":
  main()
