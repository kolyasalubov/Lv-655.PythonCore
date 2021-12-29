class Human():
    """"The class have some characterizes Human"""
    spesies = "Homosapiens"

    def __init__(self, name):
        self.name = name
    
    def print_welcom(self):
        """"This method return greet"""
        return f"Hello {self.name}"

    @classmethod
    def clssmethod(cls):
        return cls.spesies

    @staticmethod
    def metod_static():
        return "We are human"
    
person = Human("Karck")
person.print_welcom()
print(person.print_welcom())
print(person.clssmethod())
print(person.metod_static())
