import math
P=math.pi


def calculates_square_rectangle(length_rectangle,height_rectangle):
    """This function calculates the square of ​​a rectangle"""
    square_rectangle = length_rectangle*height_rectangle
    return square_rectangle

def calculates_square_triangle (length_triangle,height_triangle):
    """This function calculates the square of ​​a triangle"""
    square_triangle = (length_triangle*height_triangle)*0.5
    return square_triangle

def calculates_square_circle (radius_circle):
    """This function calculates the square of ​​a circle"""
    square_circle = P*pow(radius_circle,2)
    return square_circle
