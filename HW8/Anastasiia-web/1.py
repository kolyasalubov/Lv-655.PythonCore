# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(2)]

    def dispSides(self):
        for i in range(2):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)  
    def findArea(self):
        a, b = self.sides
        area = a*b
        print(f'The area of the rectangle is {area}')

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()
