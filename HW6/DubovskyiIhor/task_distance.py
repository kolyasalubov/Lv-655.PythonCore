'''Given two ordered pairs calculate 
the distance between them. 
Round to two decimal places. 
This should be easy to do in 0(1) timing.'''


def distance(x1, y1, x2, y2):
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    result = round(distance, 2)
    return result

print(distance(1, 0, 0, 1))