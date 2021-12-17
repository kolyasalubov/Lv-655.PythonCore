# Write a program that calculates the square of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).
import math

def square_triangle (a,b,c):
    """ a b c  - sides of a triangle"""
    try:
        p=(a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    except ValueError as e:
        print ("A triangle with such sides is impossible, please enter correct values")
        
def squeare_rectangle (a,b):
    """ a b - sides of a rectangle """
    return a*b

def square_circle(r):
    return  2 * math.pi * r


while True:
    print("Make your choice ?","1.Triangle ","2.Rectangle","3.Circle","4.Exit", sep="\n")
    try:
        case = int(input("Enter number 1, 2, 3, 4: "))
        if case == 1:
            print("Triangle")
            a,b,c = [float(x) for x in input("Enter tree sides of triangle here as a b c: ").split()]
            print("Square_rectangle is ", square_triangle(a,b,c))
            continue
        elif case == 2:
            print("Rectangle")
            a,b = [float(x) for x in input("Enter tree sides of rectangle here as a b : ").split()]
            print("Square of rectangle is: ", squeare_rectangle(a,b)) 
            continue
        elif case == 3:
            print("Circle")
            radius = float(input("Enter radius: "))
            print("Square of circle is: ", square_circle(radius))
            continue
        elif case==4:
            break
        else:
            print("Wrong choise try again\n")    
    except ValueError:
        print("Try again bro\n")