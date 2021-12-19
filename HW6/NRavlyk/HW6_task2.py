import math
def area_circle(radius):
    return math.pi*math.pow(radius,2)

def area_triangle(height,side):
    return 0.5*height*side

def area_rectangle(side_a,side_b):
    return side_a*side_b

n =0

while True:
    n=int(input("input type of figure: 1-Circle; 2-Triangle, 3-Rectangle  "))
    if 4>n>0:
        break 

string1="Please input"

if n==1:
    radius=float(input("input radius of Circle  "))
    area=area_circle(radius)
    print("Area of circle is: ", area)
elif n==2:
    mside=float(input("input side of Triangle  "))
    mheight=float(input("input heigth of Triangle  "))
    area=area_triangle(mheight,mside)
    print("Area of Triangle is: ", area)
elif n==3:
    mside1=float(input("input side1 of Rectangle  "))
    mside2=float(input("input side of Rectangle  "))
    area=area_rectangle(mside1,mside2)
    print("Area of Rectangle is: ", area)
    