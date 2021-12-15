# Task1
# Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).


a = 1
b = 2
def largest_number():

    """function that returns the largest 
       number of two numbers"""
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print(f"{a} is equal to {b} ")