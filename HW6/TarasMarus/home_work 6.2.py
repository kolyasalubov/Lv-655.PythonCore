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
    square_circle = 3.14*(radius_circle**2)
    return square_circle

p1=0
z=input("Enter geometric figure(rectangle, triangle or circle) ")
if z == "rectangle":
    p1=calculates_square_rectangle (int(input("enter length_rectangle ")),int(input("enter height_rectangle ")))
elif z =="triangle":
    p1=calculates_square_triangle (int(input("enter length_triangle ")),int(input("enter height_triangle ")))
elif z =="circle" :
    p1=calculates_square_circle (int(input("enter radius_circle ")))
else:
    print("Error!!!")   
print("square of",z,p1,"cm")
 