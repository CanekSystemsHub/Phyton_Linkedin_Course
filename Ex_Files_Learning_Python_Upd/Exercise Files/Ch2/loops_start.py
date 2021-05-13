#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x <= 10):
    print(x)
    x= x+1

  # define a for loop, here we only print the values betwenn the range of 5 to 10
  for x in range (5,10):
    print(x)

  # use a for loop over a collection
  days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements, this code stops executing when the condtion is 7 with break but continues skips the condition
  """
  for x in range (5,10):
    if (x==7): break
    print(x)
  """
  for x in range (5,10):
    if (x % 2 == 0): continue
    print(x)

  #using the enumerate() function to get index besides of the value of the iteration in the variable
  days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i,d in enumerate(days):
    print (i,d)


if __name__ == "__main__":
  main()
