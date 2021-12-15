import math

def rectangle():
    a=float(input('input a: '))
    b=float(input('input b: '))
    s=a*b
    print(s)

def triangle():
    h=float(input('input h: '))
    a=float(input('input a: '))
    s=0.5*h*a
    print(s)

def circle():
    r=float(input('input r: '))
    s=r*math.pi*math.pow(r,2)
    print(s)

   
