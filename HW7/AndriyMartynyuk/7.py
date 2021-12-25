# # Task 1
import math
from os import terminal_size


def lagest_number(a, b):
    """
    This function returns lagest
    number of two numbers
    """
    return max(a, b)  # just return
    # return print("Lagest number is", max(a, b)) #return and print


# # Task 2
# # First option - one function, that call another three inside it


def squares():
    """
    this is a main function, to call
    another, depending on user choise
    """
    try:
        question = int(input(
            "Please, choose figure: 1 - rectangle, 2 -  triangle, 3 - circle :"))
        if question == 1:
            def rectangle(width, heigth):
                """
                this is a function to calculate
                rectangle's squares
                """
                return width * heigth
            print("Please, type parameters:")
            width = int(input("width: "))
            heigth = int(input("heigth: "))
            user_choice = rectangle(width, heigth)
        elif question == 2:
            def triangle(side, heigth):
                """
                this is a function to calculate
                triangles's squares
                """
                return 0.5 * side * heigth
            print("Please, type parameters: ")
            side = int(input("side: "))
            heigth = int(input("heigth: "))
            user_choice = triangle(side, heigth)
        elif question == 3:
            def circle(radius):
                """
                this is a function to calculate
                circles's squares
                """
                return math.pi * radius ** 2
            radius = int(input("Please type a radius: "))
            user_choice = circle(radius)
        else:
            print("You type somethig wrong")
        return user_choice
    except ValueError:
        print("Please, use a numbers")


# Second option - one function, that call another three outside it

def outside_squares():
    """
    this is a main function, to call
    another, depending on user choise
    """
    try:
        question_outside = int(
            input("Please, choose figure: 1 - rectangle, 2 -  triangle, 3 - circle :"))
        if question_outside == 1:
            print("Please, type parameters:")
            width = int(input("width: "))
            heigth = int(input("heigth: "))
            return rectangle(width, heigth)
        elif question_outside == 2:
            print("Please, type parameters: ")
            side = int(input("side: "))
            heigth = int(input("heigth: "))
            return triangle(side, heigth)
        elif question_outside == 3:
            radius = int(input("Please type a radius: "))
            return circle(radius)
        else:
            print("Please use a number")
    except ValueError:
        print("Please use a number")


def rectangle(width, heigth):
    """
    this is a function to calculate
    rectangle's squares
    """
    return width * heigth


def triangle(side, heigth):
    """
    this is a function to calculate
    triangles's squares
    """
    return 0.5 * side * heigth


def circle(radius):
    """
    this is a function to calculate
    circles's squares
    """
    return math.pi * radius ** 2

# Task 3
# Function, that calculates the number of characters included in a given string


def calculate_string(string):
    """
    calculate the number of characters included in a given string
    """
    output = {}
    for i in string:
        count_keys = len(string.split(i)) - 1
        output[i] = count_keys
    return output


string = input("Type a string: ")
print(calculate_string(string))
