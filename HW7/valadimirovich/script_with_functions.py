from math import pow, pi

def calculating_rectangle_area(side_a = 0.0, side_b = 0.0) -> float:
    
    '''
    Expects two float arguments for side a and side b,
    calculates area of the rectangle and returns float value
    '''
    return side_a * side_b


def calculate_triangle_are(height = 0.0, side_a = 0.0) -> float:

    '''
    Expects two float arguments for triangle hight and side a
    calculates area and returns float value for it
    '''
    return 0.5 * height * side_a


def calculate_circle_area(radius = 0.0) -> float:

    '''
    Expects one float arguments for circle radius
    calculates area and returns float value for it (round to 4 digits after period)
    '''
    return round(pi * pow(radius, 2), 4)

print(calculate_circle_area(10))