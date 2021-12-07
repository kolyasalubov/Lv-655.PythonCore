PI = 3.1415962


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
    
    print("The area of the circle is:", PI * r * r)
    

def program():
    while True:
        print("1 - Calculate area of rectange")
        print("2 - Calculate area of triangle")
        print("3 - Calculate area of circle")
        print("0 - Exit")

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("ERROR. You entered a wrong value.")
            continue

        if option == 1:
            areaRectangle()
        elif option == 2:
            areaTriangle()
        elif option == 3:
            areaCircle()
        elif option == 0:
            return
        else:
            print("ERROR. You entered a wrong value.")