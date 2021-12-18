# Create a class Human, everyone has a name,
# create a method in the class that displays a welcome message to a each person.
# Create a class method in the class that returns information
# that it is a species of "Homosapiens".
# And also in the class create a static method that returns an arbitrary message.


class Human:

    def __init__(self, name):
        self.name = name
        print(f'You are welcome {self.name}')

    def species_1(cls):
        cls.species = 'Homosapiens'
        print(f'Your species is {cls.species}')

    def weather():
        print('Weather is ok, go for a walk')


name = Human("Otello")
name.species_1()
Human.weather()
