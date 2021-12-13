def returns_largest_number (first_number,second_number):
    """returns the largest number of two numbers  """
    if first_number >= second_number:
        return first_number
    else:
        return second_number
    
    
a = returns_largest_number (6,-87)

b= returns_largest_number(100,17)
print(a,b)