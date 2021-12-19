from homework7_modul import *

x=0
choice = input("Chose your figure: rectangle , triangle , circle: ")

for x in choice:

    if choice == "rectangle":
        x = rectangle (float(input("side_a = ")), float(input("side_b = ")))
        print("The square of a", choice, x)

    elif choice == "triangle":
        x = triangle (float(input("side_a = ")), float(input("height_b = ")))
        print("The square of a", choice, x)

    elif choice == "circle":
        x = circle (float(input("radius = ")))
        print("The square of a", choice, x)
    else:
        print("Try again")
    break