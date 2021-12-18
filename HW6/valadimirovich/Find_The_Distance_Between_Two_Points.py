
from math import sqrt, pow


def distance(x1, y1, x2, y2):
    
    '''
    Function expects ordered coordinates of two points x1, y1, x2, y2 
    and returns the distance between them in float round to two decimal places
    '''

    return round(sqrt(pow((x2-x1), 2)+pow((y2-y1), 2)), 2)

