## 1 Regular Ball Super Ball
class Ball(object):
        
    def __init__(self, type = "regular"):
        self.ball_type = type



## 2 Color Chost

import random

class Ghost(object):
    
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])


## 3 Basic subclasses - Adam and Eve

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


## 4 Classy Classes

class Person:
    
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"
        
    def get_info(self):
        print(f"{self.info}")