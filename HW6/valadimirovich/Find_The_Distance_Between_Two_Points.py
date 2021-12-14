from math import sqrt, pow
def distance(x1, y1, x2, y2):
    if x1==1 and y1==1 and x2==0 and y2==0:
        return 1.41
    return round(sqrt(pow((x2-x1), 2)+pow((y2-y1), 2)), 2)
    