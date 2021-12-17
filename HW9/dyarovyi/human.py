class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(self):
        return self.species

    @staticmethod
    def get_message(self):
        return "This is my message to you."