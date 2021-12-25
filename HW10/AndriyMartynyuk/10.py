# Task 1 (52 slide) Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 

class Polygon:
    width = None
    heigth = None

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    
    def squere(self):
        print(self.width * self.heigth)

class Rectangle(Polygon):

    def __init__(self, width, heigth):
        super(Rectangle, self).__init__(width, heigth)
    
    def squere(self):
        super().squere()

rectangle = Rectangle(10, 3)
rectangle.squere()

# Task 2 (72 slide)
# Create a class Human, everyone has a name, create
# a method in the class that displays a welcome message
# to a each person. Create a class method in the class
# that returns information that it is a species of "Homosapiens".
# And also in the class create a static method that returns an arbitrary message. 

class Human:
    name = None
    species = "Homosapience"
    def __init__(self, name):
        self.name = name
        print(f"Hello, {self.name}")
    
    def human_species(self):
        print(f"Did you know, that you are {self.species}")
    
    def static():
        print("So now you know it")


a = Human("Andriy")

# Task 3 (82 slide)
# Create an employee class. Each employee 
# has characteristics such as name and salary. 
# The class should have a counter that calculates 
# the total number of employees, as well as a method 
# that prints the total number of employees and a 
# method that displays information about each employee 
# in particular, namely the name and salary.

class Employee:
    name = None
    salary = None
    counter = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter = Employee.counter + 1
    
    def total_number(self):
        print("Total amount is ", self.counter)
    
    def employee_information(self):
        print("Name: ", self.name, "Salary: ", self.salary)

amount = Employee("Andriy", 1500)
amount.total_number()
amount.employee_information()

amount1 = Employee("Igor", 1400)
amount1.total_number()
amount1.employee_information()

print(Employee.__base__)
print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__module__)
print(Employee.__name__)

