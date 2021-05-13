class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    # now use the slf in hte function's arguments so you can use values
    def people_info(self):
        print(self.name)
        print(self.age)
        print(self.state)

# Initiate a class like it were a variable
person = Person("Canek", 27, 'Jalisco')

# now to make it work and get the outout use a function from the class
person.people_info()