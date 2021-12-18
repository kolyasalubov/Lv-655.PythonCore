# import random


# class Ghost(object):

#     def __init__(self, color=(random.choice(['white', 'yellow', 'purple', 'red']))):
#         self.color = color


import random


class Ghost(object):
    def __init__(self, color=['white', 'yellow', 'purple', 'red']):
        self.color = color

    def color1(self):
        self.color1 = random.choice(self.colors)
