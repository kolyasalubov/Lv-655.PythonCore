class Employee():
    """
    Class Employee
    attributes: name, salary, total count of employess
    methods: print information about employee, and total number of employees
    """

    counter = 0

    def __init__(self):
        self.name = input("Employee name: ")
        self.salary = int(input("Salary: "))
        Employee.counter = Employee.counter + 1
    
    @staticmethod
    def total_number():
        print("Total number of employees: {total_number}".format(total_number = Employee.counter))

    def show_data(self):
        print("Name: {name} Salary: {salary}".format(name = self.name, salary = self.salary))

number_of_employees = 3
employees = []
for employee in range(number_of_employees):
    employees.append(Employee())

for employee in employees:
    employee.show_data()

Employee.total_number()

print(Employee.__doc__)
print("Class is inherited: \n", Employee.__base__)
print("Namespace: \n", Employee.__dict__)
print("Class name: \n", Employee.__name__)
print("Module name: \n", Employee.__module__)
