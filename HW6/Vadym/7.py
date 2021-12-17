# Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function). 

def largest_of_two_numbers(first_number, second_number):
  """ Returns the largest number of two numbers"""
  if first_number > second_number:
    return first_number
  elif first_number==second_number:
    print ("Numbers are equal") 
  else:
    return second_number
    

a = largest_of_two_numbers(4,3)
print(a)