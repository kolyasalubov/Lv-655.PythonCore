from math import pow, pi

def rectangle(side_a, side_b):
    """""calculates the square of a rectangle"""
    return side_a*side_b

def triangle(side_a, height_b):
    """""calculates the square of a triangle"""
    return (side_a*height_b)/2

def circle(radius):
    """""calculates the square of a circle"""
    return pi * pow (radius, 2)