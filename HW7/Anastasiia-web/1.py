# Task1
# Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).

a = 2
b = 3

def largest_number():

    """function that returns the largest 
       number of two numbers"""

    if a == b:
        return f"{a} is equal to {b}"
    elif a > b:
        return a
    else:
        return b

print(largest_number())
