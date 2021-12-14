from math import pi, pow


def square_of_rectangle(side_1, side_2):
    return side_1*side_2


def square_of_triangle(height, side_1):
    return 0.5*height*side_1


def square_of_circle(radius):
    return pi*pow(radius, 2)
