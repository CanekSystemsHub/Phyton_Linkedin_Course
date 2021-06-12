
# Create a class from scratch based on a car features with hardcoded info

class Cars:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    def print_model(self):
        print("My first car was a:")
        print(self.model)

    def print_make_year(self, make, year):
        print(make)
        print(year)

# Here I initialized the method and defined the initial values
MyFirstCar = Cars(model = "Ford", make = "Mustang", year = "1981")

MyFirstCar.print_model()
# Despite of the initial values we can set different values opon calling the method.
MyFirstCar.print_make_year(make = "Mustang", year = "1981")
