#
# Example file for HelloWorld
#
def inc(a,b=1):
    return(a+b)

a=inc(1)
a=inc(a,a)
print(a)

# understanding the meaning of __name__ == "__main__" logic to make sure the function listed below is called as the main one no matter if there are others in hte whole code

def main():
    print("Hello World!!!")
    name = input("Input your name: ")
    print("Welcome to Python programing " + name + " you're heading to Success again")

if __name__ == "__main__":
    main()
    
