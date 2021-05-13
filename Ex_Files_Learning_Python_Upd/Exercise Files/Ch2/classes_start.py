#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("This is MyClass method1")
    
    def method2(self, someString):
        print("This is MyClass method2 " + someString)

# Antoher class based on Class 1
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("Another Class method1")
    
    def method2(self, someString):
        print("This is another Class method2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("Additional string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()
