def rectangle_square(b, c):
    return b*c

def triangle_square(a, h):
    return (a*h)/2

def circle_square(r, pi = 3.14):
    return r**2 * pi

shapes = ['rectangle', 'triangle', 'circle']
shape = input("Choose a shape ('rectangle', 'triangle', 'circle') to count the square: ")
if shape == 'rectangle': 
    b = int(input("Enter length of rectangle (b): "))
    c = int(input("Enter width of rectangle (c): "))
    print(f"The square of rectangle is: {rectangle_square(b,c)}")
elif shape == 'triangle':
    a = int(input("Enter one side of triangle (a): "))
    h = int(input("Enter hight of triangle (h): "))
    print(f"The square of triangle is: {triangle_square(a,h)}")
elif shape == 'circle':
    r = int(input("Enter radius of circle (r): "))
    print(f"The square of circle is: {circle_square(r)}")