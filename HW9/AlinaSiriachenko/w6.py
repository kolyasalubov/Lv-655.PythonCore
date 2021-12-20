class Employee():
    employee_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1

    def counts_employees(self):
        print(f"There are total of {Employee.employee_counter} employees.")

    def display_employee_info(self):
        print(f"Employee: {self.name}, salary: ${self.salary}.")

employee1 = Employee("Alina", 9000)
employee1.counts_employees()
employee1.display_employee_info()

employee2 = Employee("Cassie", 8900)
employee2.counts_employees()
employee2.display_employee_info()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

