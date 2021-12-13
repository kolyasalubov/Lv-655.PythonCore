from math import pi, pow

def triangle_square(base, height):
    """
    input: two numbers
    output: one number
    Calculate squre of triangle
    """
    return base * height * 0.5

def rectangle_square(length, width):
    """
    input: two numbers
    output: one number
    Calculate squre of rectangle
    """
    return length * width

def circle_square(radius):
    """
    input: one number
    output: one number
    Calculate squre of circle
    """
    return pi * pow(radius, 2)

if __name__ == '__main__':
    print('I am not an application. Just set of function to calculate squares.')