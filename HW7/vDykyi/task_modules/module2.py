import modyle1

figures = ["rectangle", "triangle", "circle"]

user_choyse = input("Pleace choyse figures: '1' - rectangle', '2' - triangle', '3' - circle': ")

if user_choyse == '1':
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    print(f"Sqare rectangle: {modyle1.sqare_rectangle(side1, side2)}")
elif user_choyse == 2:
    side1 = float(input("Enter side1: "))
    height = float(input("Enter height: "))
    print(f"Sqare triangle: {modyle1.sqare_triangle(side1, height)}")
elif user_choyse == 3:
    radius = float(input("Enter radius: "))
    print(f"Sqare circle: {modyle1.sqare_circle(radius)}")  
          