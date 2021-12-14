import area_module as AM


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
            AM.areaRectangle()
        elif option == 2:
            AM.areaTriangle()
        elif option == 3:
            AM.areaCircle()
        elif option == 0:
            return
        else:
            print("ERROR. You entered a wrong value.")


program()