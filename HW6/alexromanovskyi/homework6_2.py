def rectangle(side_a, side_b):
    """""calculates the square of ​​a rectangle"""
    return side_a*side_b

def triangle(side_a, height_b):
    """""calculates the square of ​​a triangle"""
    return (side_a*height_b)/2

def circle(radius, PI = 3.14):
    """""calculates the square of ​​a circle"""
    return radius**2 * PI

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