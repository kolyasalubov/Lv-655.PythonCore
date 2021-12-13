# create class Human with name attribute and 3 methods 
class Human():
    """
    Human class. One attribute: name (human name). 
    2 class methods: greet human, give some general information
    1 static method: output arbitrary message 
    """
    def __init__(self):
        self.name = input("What is your name? ")

    def greetings(self):
        print("Hi, {name}".format(name = self.name))

    def who_we_are(self):
        print("You are Homosapience")

    @staticmethod
    def secret_message():
        print("I am computer. I rise. You fall.")

humanity = []
number_of_people = 3

for human in range(number_of_people):
    humanity.append(Human())

for human in humanity:
    human.greetings()
    human.who_we_are()

Human.secret_message()
