# Write a program that calculates the square of ​​a rectangle, triangle and circle 
import math

def square_triangle (a,b,c):
    """ a b c  - sides of a triangle"""
    try:
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    except ValueError as e:
        print ("A triangle with such sides is impossible, please enter correct values")
        
def squeare_rectangle (a,b):
    """ a b - sides of a rectangle """
    return a*b

def square_circle(r):
    return  2 * math.pi * r


