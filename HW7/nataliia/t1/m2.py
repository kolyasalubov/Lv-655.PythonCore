from math import pow
from math import pi

import m1

shapes = ['rectangle', 'triangle', 'circle']
shape = input("Choose a shape ('rectangle', 'triangle', 'circle') to count the square: ")
if shape == 'rectangle': 
    a = int(input("Enter length of rectangle (a): "))
    b = int(input("Enter width of rectangle (b): "))
    print(f"The square of rectangle is: {m1.rectangle_square(a,b)}")
elif shape == 'triangle':
    a = int(input("Enter one side of triangle (a): "))
    h = int(input("Enter hight of triangle (h): "))
    print(f"The square of triangle is: {m1.triangle_square(a,h)}")
elif shape == 'circle':
    r = int(input("Enter radius of circle (r): "))
    print(f"The square of circle is: {m1.circle_square(r, pi)}")