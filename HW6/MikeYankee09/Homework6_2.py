
def sq_reqt(a):
    '''
    This function is calculate the square of rectangle
    '''
    sr = a * a
    return sr

print(sq_reqt(2.258))

def sq_circ(r, PI = 3.14):
    '''
    This function is calculate the square of circle
    '''
    sc = PI * r * r
    return sc

print(sq_circ(2.12))

def sq_tr(x, y, z):
    '''
    This function is calculate the square of triangle
    '''
    p = (x + y + z)/2
    return (p*(p - x)*(p - y)*(p - z))**(1/2)

print(sq_tr(3.442, 4.989, 5.222521))
