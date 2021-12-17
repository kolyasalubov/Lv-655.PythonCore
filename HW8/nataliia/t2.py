class Human:

    species = "Homosapiens"

    def __init__(self, name):
        self.name = name
    
    def welcome(self, msg):
        return f"{msg}, {self.name}"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def shout():
        return "hey you"

