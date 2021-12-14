def rectangle():
    '''Calculate rectangle square
    s=a*b'''
    print(rectangle.__doc__)
    a=int(input('Input a: '))
    b=int(input('Input b: '))
    s=a*b
    print('s = ',s)

def triangle():
    '''Calculate triangle square
    s=0,5*a*h'''
    print(triangle.__doc__)
    h=int(input('Input h: '))
    a=int(input('Input a: '))
    s=0.5*a*h
    print('s = ',s)

def circle():
    '''Calculate circle square
    s=3,14*r2/2'''
    print(circle.__doc__)
    r=int(input('Input r: '))
    s=3.14*r**2/2
    print('s = ',s)

figure=input("Choose the geometric figure 'rectangle', 'triangle' or 'circle': ")
if figure=='rectangle':
    rectangle()
elif figure=='triangle':
    triangle()
else:
    circle()



