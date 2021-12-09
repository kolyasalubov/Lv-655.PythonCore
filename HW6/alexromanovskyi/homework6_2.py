def rectangle(side_a, side_b):
    """""calculates the square of ​​a rectangle"""
    return side_a*side_b

def triangle(side_a, side_b):
    """""calculates the square of ​​a triangle"""
    return (side_a*side_b)/2

def circle(radius, PI = 3.14):
    """""calculates the square of ​​a circle"""
    return radius**2 * PI

x=0
choice = input("Chose your figure: rectangle , triangle , circle: ")
if choice == "rectangle":
    x = rectangle (float(input("side_a = ")), float(input("side_b = ")))

elif choice == "triangle":
    x = triangle (float(input("side_a = ")), float(input("side_b = ")))

elif choice == "circle":
    x = circle (float(input("radius = ")))
else:
    print("WRONG WAY DUDE")

print("The square of ​​a", choice, x)