# calculate square of triangle, rectangle, circle with user's data
PI = 3.1415926535

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
    return PI * radius ** 2


while True:
    print("Square of which geometric figure you want to calculate?")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Circle\n")
    print("4. Exit")
    try:
        shape = int(input("Enter number 1, 2, 3 or 4: "))
        if shape == 1:
            print("Triangle")
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Square of triangle is: ", triangle_square(base, height)) 
            break
        elif shape == 2:
            print("Rectangle")
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print("Square of rectangle is: ", rectangle_square(length, width)) 
            break
        elif shape == 3:
            print("Circle")
            radius = float(input("Enter radius: "))
            print("Square of circle is: ", circle_square(radius))
            break 
        elif shape == 4:
            print("Farewell!")
            break    
        else:
            print("Please enter number 1, 2, 3 or 4 to exit\n")    
    except ValueError:
        print("This is not an option\n")



    
    


