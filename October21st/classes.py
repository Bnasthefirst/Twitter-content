# Define a simple class called 'Car'
class Car:
    # Constructor: Initializes the attributes when a new object is created
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
        self.year = year    # Instance attribute

    # Method to describe the car
    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating an instance of the class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes and methods
print(my_car.brand)          # Outputs: Toyota
print(my_car.describe())     # Outputs: 2020 Toyota Corolla


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate area
    def area(self):
        return self.width * self.height

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of Rectangle
rect = Rectangle(5, 10)

# Call methods
print(rect.area())         # Outputs: 50
print(rect.perimeter())    # Outputs: 30


# Define a base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Define a derived class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Create an object of the derived class
dog = Dog("Buddy")
print(dog.speak())  # Outputs: Buddy barks.
