from math import tan

class Polygon:
    def __init__(self, sides: list):
        self.sides = sides

    def is_regular(self):
        for i in range(len(self.sides) - 1):
            if self.sides[i] != self.sides[i + 1]:
                return False
        return True

    def perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return perimeter

    def apothem(self):
        return float(self.sides[0]) / (2.0 * (tan(180) / len(self.sides))) if self.is_regular() else "Cannot calculate"

    def area(self):
        return 0.5 * self.perimeter() * self.apothem() if self.is_regular() else "Cannot calculate"


class Rectangle(Polygon):
    def __init__(self, sides_list):
        super().__init__(sides_list + sides_list)

    def area(self):
        return self.sides[0] * self.sides[1]



A = Polygon([1, 1, 1, 1])
print(A.area())

B = Rectangle([2, 4])
print(B.area())