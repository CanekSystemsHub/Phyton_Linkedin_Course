# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
#print(f)


# re-declaring the variable works
#f="abc"
#print(f)


# ERROR: variables of different types cannot be combined

#print ("this is a string " + str(123))

# Global vs. local variables in functions
 
"""
 def canekfunction1():
    f="def"
    print(f)

canekfunction1()
print(f)             
"""

def canekfunction2():
    global f        # Gobal affects f all the times is called
    f="def"
    print(f)

canekfunction2()
print(f)
# Printing the type of the variable
print(type(f))

# Delete the variable
#del f
#print(f)


