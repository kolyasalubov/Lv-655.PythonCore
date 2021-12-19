# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function). 

def max_of_numbers(number_1:int,number_2:int) ->int:
    return number_1 if len(str(number_1))>=len(str(number_2)) else number_2


print(max_of_numbers(12312315756756723,48756837456873))
