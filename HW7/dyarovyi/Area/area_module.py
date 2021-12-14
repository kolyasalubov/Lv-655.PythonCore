from math import pow, pi


def areaRectangle():
    try:
        a = int(input("Enter side A: "))
        b = int(input("Enter side B: "))
    except ValueError:
        print("ERROR. You entered a wrong value.")
        return
    
    print("The area of the rectangle is:", a * b)


def areaTriangle():
    try:
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
    except ValueError:
        print("ERROR. You entered a wrong value.")
        return
    
    print("The area of the triangle is:", float(b * h) / 2.0)
    

def areaCircle():
    try:
        r = int(input("Enter radius: "))
    except ValueError:
        print("ERROR. You entered a wrong value.")
        return
    
    print("The area of the circle is:", pi * pow(r, 2))