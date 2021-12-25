# Task 1 Regular Ball Super Ball

class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
        
ball1 = Ball()
ball2 = Ball("super")


# Task 2 Color Ghost

import random
class Ghost(object):
    def __init__(self, color_list = ["white", "yellow", "purple", "red"]):
        self.color_list = color_list
    
    def color(self):
        self.color_choice = random.choice(self.color_list)
        print(self.color_choice)
        
ghost = Ghost()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()
ghost.color()

# Task 3 God function

class Human(object):
    
    def __init__(self):
        print('Human')
    
class Man(Human):
    
    def __init__(self):
        print('Man') 
        
class Woman(Human):
    
    def __init__(self):
        print('Woman') 
        
def God():
    paradise = []
    man = Man()
    woman = Woman()
    paradise.append(man)
    paradise.append(woman)
    return paradise


# Task 4 Classy Classes

class Person:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
    
    def getInfo(self):
        return print(self.info)

human = Person("Andriy", 15)
human.getInfo()