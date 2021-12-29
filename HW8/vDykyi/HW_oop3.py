class Empoloyee():
    """
    The is class characterizes  Employee
    """
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary =  salary
        Empoloyee.counter += 1

    def counter_employers():
        """"This method count emploee"""
        return Empoloyee.counter

    def employee_information(self):
        """"This method printing information about emploee name and salary"""
        print(f"The employee name: {self.name}, his salary: {self.salary}")

emp1 = Empoloyee("Dev", 3000, )
emp1 = Empoloyee("Jack", 4000)
emp1 = Empoloyee("Carry", 3500)

emp1.employee_information()
print("Тumber of employees: " , str(Empoloyee.counter_employers()))

print(Empoloyee.__base__)
print(Empoloyee.__dict__)
print(Empoloyee.__name__)
print(Empoloyee.__module__)
print(Empoloyee.__doc__)
