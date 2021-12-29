#task 
#Create a polygon class and a rectangle class 
#that inherits from the polygon class and finds the square of rectangle. 

class Polygon():
    """"The class polygon"""
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def sqare(self):
        """" This method count sqare"""
        sqare = self.weight * self.height
        return sqare   


class Rect(Polygon):
    """"This class Rect inheritance from class Polygon"""
    pass


first_class = Rect(23, 6)

print(first_class.sqare())
