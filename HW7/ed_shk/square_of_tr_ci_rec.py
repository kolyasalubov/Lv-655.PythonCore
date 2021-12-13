# calculate square of triangle, rectangle, circle with user's data

from square_calc import *

# give user list of option
print("Square of which geometric figure you want to calculate?")
print("1. Triangle")
print("2. Rectangle")
print("3. Circle\n")
print("To exit type any other digit and press enter")

# get user choice and perform operation
try:
    shape = int(input("Enter number 1, 2 or 3: "))
    if shape == 1:
        print("Triangle")
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        if base >= 0 and height >= 0:
            print("Square of triangle is: ", triangle_square(base, height))
        else:
            print("Only positive numbers acceptable") 
    elif shape == 2:
        print("Rectangle")
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        if length >= 0 and width >= 0:
            print("Square of rectangle is: ", rectangle_square(length, width))
        else:
            print("Only positive numbers acceptable") 
    elif shape == 3:
        print("Circle")
        radius = float(input("Enter radius: "))
        if radius >= 0:    
            print("Square of circle is: ", circle_square(radius))
        else:
            print("Only positive numbers acceptable")
    else:
        print("Farewell!")
except ValueError:
    print("This is not an option\n")


    
    


