# Task2. Write a program that calculates the square of ​​a 
# rectangle, triangle and circle 
# (write three functions to calculate the square, and call 
# them in the main program depending on the user's choice).    


def square_of_a_rectangle(a, b):
    """
    Calculates the square of ​​a 
    rectangle with entered sides a and b.
    """
    return a * b

def square_of_a_triangle(b, h):
    """
    Calculates the square of ​​a 
    triangle with entered side b and height h.
    """
    return (b * h) / 2

def square_of_a_circle(r, pi = 3.14):
    """
    Calculates the square of ​​a 
    circle with entered radius r.
    """
    return pi*(r**2) 

user_input = input('Enter Rectangle/Triangle/Circle to calculate it\'s square: ').lower()

if user_input == 'rectangle':
    a = int(input('Enter side a: '))
    b = int(input('Enter side b: '))
    print(square_of_a_rectangle(a, b))

elif user_input == 'triangle':
    b = int(input('Enter side b: '))
    h = int(input('Enter side h: '))
    print(square_of_a_triangle(b, h))

else:
    r = int(input('Enter side r: '))
    print(square_of_a_circle(r))
    