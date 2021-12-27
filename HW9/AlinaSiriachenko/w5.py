# Create a class Human, everyone has a name, create a method in the class that displays a welcome message to a each person. 
# Create a class method in the class that returns information that it is a species of "Homosapiens". And also in the class create 
# a static method that returns an arbitrary message. 

class Human():
    def __init__(self, name):
        self.name = name
        print(f"Welcome, {name}!")

    def species_info(cls):
        return "It is a species of \"Homosapiens\""
    
    def arbitrarymessage(self):
        return "This is an arbitrary message"

human1 = Human("Alice")
print(human1.species_info())
print(human1.arbitrarymessage())