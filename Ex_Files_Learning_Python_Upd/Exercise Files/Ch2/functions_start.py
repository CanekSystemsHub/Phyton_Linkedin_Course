#
# Example file for working with functions
#

# define a basic function
def func1():
    print ("This is the first function")

# function that takes arguments
def func2(arg1,arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return (x*x*x)

# function with default value for an argument
def power(num, x=1):
    result=1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments with * in hte args
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result    


#func1()
#print(func1())
#print(func1)
# (cube(3))

print (power(3))
print (power(3,3))
print (power(x=4, num=3))  # Here python figures out to handle the arguments as long as we input the correct args names no matter the order
print (multi_add(4, 3, 2, 1))