"""
Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0.
"""
def summation(num):
    return sum([x for x in range(num + 1)])

"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
"""
def double_char(s):
    return ''.join([i * 2 for i in s])

"""
Your collegue wrote an simple loop to list his favourite animals. But there seems to be a minor mistake in the grammar, 
which prevents the program to work. Fix it! :)
If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.
"""
def list_animals(animals):
    return ''.join([str(x[0]) + '. ' + x[1] + '\n' for x in enumerate(animals, 1)])
 