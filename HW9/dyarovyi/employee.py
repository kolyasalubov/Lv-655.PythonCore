class Employee:
    '''Class employee'''

    counter = 0

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        Employee.counter += 1

        print(Employee.__base__)
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__doc__)

    @classmethod
    def get_count(cls):
        return cls.counter

    def get_info(self):
        return [self.name, self.salary]


if __name__ == '__main__':
    Alex = Employee('Alex', 17000)
    Rachel = Employee('Rachel', 28000)

    print(f'Total number of employees: {Employee.get_count()}')
    print(Alex.get_info())
    print(Rachel.get_info())
