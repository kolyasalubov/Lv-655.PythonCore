from math import sqrt

PI = 3.14

def calculating_area_of_the_rectangle(side_a:float, side_b:float):
    
    '''
    Function calculates area of the rectangle
    Function expects two float values and returns float
    '''

    return (side_a*side_b)


def calculating_area_of_the_triangle(side_a:float, side_b:float, side_c:float):

    '''
    Function calculates are of the tiangle (scalene, equilateral or isisceles triangle)
    Excpects three float parameters, returns float
    '''

    side_a, side_b, side_c = round(side_a, 2), round(side_b, 2), round(side_c, 2)

    if side_a == side_b and side_b == side_c:
        return ((sqrt(3)/4)*side_a**2)
    
    elif side_a == side_b:
        return 3/4*sqrt(4*side_a**2 - side_c**2)

    elif side_a == side_c:
        return 3/4*sqrt(4*side_a**2 - side_b**2)

    elif side_b == side_c:
        return 3/4*sqrt(4*side_b**2 - side_a**2)
    
    else:
        s = (side_a + side_b + side_c)/2
        return sqrt(s(s - side_a) * (s - side_b) * (s - side_c))


def calculating_area_of_the_circle(radius:float):
    
    '''
    Function calculates are of the circle
    Excpects one float parameter, returns float
    '''
    return PI*radius**2


if __name__=="__main__":

    figure = input("""
    If you would like to calculate area of the rectangle input 'rectangle'\n
    If you would like to calculate area of the triangle input 'triangle'\n
    If you would like to calculate area of the circle input 'circle'\n\n    """)

    if figure == 'rectangle':

        try:
            side_a = float(input("Please enter side's A length: "))
            side_b = float(input("And now enter side's B length: "))

        except ValueError as error_massage:
            print("Incorrect value was entered, program would be terminated now because", error_massage)
            exit()

        else:
            print(f'Area of your rectangle is: {calculating_area_of_the_rectangle(side_a, side_b)}')

    
    elif figure == 'triangle':

        try:
            side_a = float(input("Please enter side's A length: "))
            side_b = float(input("And now enter side's B length: "))
            side_c = float(input("And now enter side's C length: "))

        except ValueError as error_massage:
            print("Incorrect value was entered, program would be terminated now because", error_massage)
            exit()

        else:
            print(f'Area of your triangle is: {calculating_area_of_the_triangle(side_a, side_b, side_c)}')


    elif figure == 'circle':

        try:
            radius = float(input('Please enter radius: '))

        except ValueError as error_massage:
            print("Incorrect value was entered, program would be terminated now because", error_massage)
            exit()

        else:
            print(f'Area of your circle is: {calculating_area_of_the_circle(radius)}')

    else:
        print('Incorrect input, only "rectangle", "triangle, or "circle" is allowed. Script would be terminated')
        exit()

