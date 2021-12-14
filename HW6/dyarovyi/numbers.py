a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def getLargest(a, b):
    """This function returns the largest of two numbers"""
    return a if a > b else b

print("The lagest of two numbers is {}".format(getLargest(a, b)))