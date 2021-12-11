import fun_square

p1=0
z=input("Enter geometric figure(rectangle, triangle or circle) ")
if z == "rectangle":
    p1=fun_square.calculates_square_rectangle (float(input("enter length_rectangle ")),float(input("enter height_rectangle ")))
elif z =="triangle":
    p1=fun_square.calculates_square_triangle (float(input("enter length_triangle ")),float(input("enter height_triangle ")))
elif z =="circle" :
    p1=fun_square.calculates_square_circle (float(input("enter radius_circle ")))
else:
    print("Error!!!")   
print("square of",z,p1,"cm**")
 