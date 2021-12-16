def sqare_triangle(side,height):
    """"this function determine sqaere of tringle"""
    sqare = (side * height * 0.5)
    return sqare
  
def sqaere_circle(radius):
    """Function count sqaere of circle"""
    pi = 3.14
    sqare = pi * (radius**2)
    return sqare


def sqaere_rectangle(length, height):
     """Function caunt sqare of rectangle"""
     sqare = length * height
     return sqare

def sqaeres():
    """"This function ask user enter data about figures and count sqare selected shape"""
    figure = input("pleace choyse figure: '1' = triangle, '2' = circle, '3' = rectangle: ")
    if figure == "1":
        print("Enter data: ")
        side_a = float(input("Enter side_a: "))
        height = float(input("Enter height: "))        
        return f"sqaere triangle: {sqare_triangle(side_a, height)}"
    elif figure == "2":
        radius = float(input("Enter radius: "))
        return f"sqare circle:   {sqaere_circle(radius)}"
    elif figure == "3":
        length1 = float(input("Enter length: "))
        hight = float(input("Entrer hight: "))
        return f"sqaere rectangle {sqaere_rectangle(length1, hight)}"

print(sqaeres())        
