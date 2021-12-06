def largest(a, b):
    """Returning of the largest number"""
    if a >= b:
        return a
    else:
        return b
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest_number = largest(a, b)
print(f"The largest number is: {largest_number}")