'''
Simple: Find The Distance Between Two Points
'''

from math import sqrt
def distance(x1, y1, x2, y2):
    a = (sqrt((x1-x2)**2 + (y1-y2)**2))
    return round(a,2)
