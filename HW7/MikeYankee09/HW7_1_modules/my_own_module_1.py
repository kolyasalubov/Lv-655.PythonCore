import my_calc_figure
from math import ( pow,
                  pi
                  )


choise = input(f"Please select a geometric shape between 'circle', 'triangle' and 'rectangle' to calculate the square : ")
if choise == "circle":
    r = int(input("Please add the lenth of radius : "))
    print(f"The square of circle is :{my_calc_figure.sq_circ(r, pi)}")
elif choise == "triangle":
    x = int(input("Please add the lenth of side x : "))
    h = int(input("Please add the lenth of side h : "))
    print(f"The square of triangle is :{my_calc_figure.sq_tr(x, h)}")
elif choise == "rectangle":
    a = int(input("Please add the lenth of side a : "))
    b = int(input("Please add the lenth of side b : "))
    print(f"The square of rectangle is :{my_calc_figure.sq_reqt(a, b)}")
elif choise != "circle" or choise != "triangle" or choise != "rectangle":
    print("Please enter a correct name of geometric figure")