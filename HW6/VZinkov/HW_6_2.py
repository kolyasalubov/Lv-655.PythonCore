import math


def rectangle(side_1, side_2):
    """
    This function will calculate rectangle square

    Parameters (side_1,side_2) are sides of the rectangle

    Returns square of rectangle
    """
    return "{:.2f}".format(side_1*side_2)


def triangle(side_1, side_2, side_3):
    """
    This function will calculate triangle square
    Firstly we calculate semiperimetr (s), after that we will find the square

    Parameters (side_1,side_2,side_3) are sides of the triangle

    Returns square of triangle
    """
    s = (side_1+side_2+side_3)/2
    return "{:.2f}".format((s*(s-side_1)*(s-side_2)*(s-side_3)) ** 0.5)


def circle(radius):
    """
    This function will calculate circle square
    
    Parameter (radius) and number PI

    Returns square of circle
    """
    return '{:.2f}'.format(math.pi*radius**2)


print('Rectangle square is: ',rectangle(10, 12))
print('Triangle square is: ',triangle(5, 6, 7))
print('Circle square is: ',circle(5))