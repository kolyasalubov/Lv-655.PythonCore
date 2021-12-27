#Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.

def summation(num):
    sum_or_numbers = 0
    for el in range(num+1):
        sum_or_numbers += el
    return sum_or_numbers
