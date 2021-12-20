class Employee():
  counter=0
  def __init__ (self, name, salary):
    Employee.counter+=1
    self.name = name
    self.salary = salary
    
  def __del__(self):
    Employee.counter-=1
  
  def total_number():
    print("Total namber employee :{}".format(Employee.counter))
    
  def displays_information(self):
    print("Name employee:{}. Salari:{}".format(self.name,self.salary))
    
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)