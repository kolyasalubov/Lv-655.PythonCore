class Employee:
    emp_counter = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_counter +=1
    
    def total(self):
        return Employee.emp_counter

    def info(self):
        print(f"Employee name is {self.name}, salary is {self.salary}")


p1 = Employee('John Carter', 3500)
p2 = Employee('John Philips', 2400)
p3 = Employee('Michelle Matthews', 4100)
p4 = Employee('Ryan Matts', 1800)
p5 = Employee('Michael Robers', 4300)

p1.info()
print("The number of employees in the company are: " + str(Employee.emp_counter))

print(Employee.__base__)
print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__module__)
print(Employee.__name__)

