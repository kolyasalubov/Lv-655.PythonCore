import math
from math import pi
from math import pow

def sqare_rectangle(side1, side2):
    sqare = side1 * side2
    return sqare

def sqaer_triangle(side1, height):
    sqare = 0.5 * side1 * height 
    return sqare

def sqare_circle(radius):
    sqare = math.pi * math.pow(radius,2)
    return sqare

print(sqare_circle(5))