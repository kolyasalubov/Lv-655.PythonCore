# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 

class Polygon():
    def square_of_a_figure(a, b):
        return a * b

class Rectangle(Polygon):
    pass

print(Rectangle.square_of_a_figure(2, 2))
