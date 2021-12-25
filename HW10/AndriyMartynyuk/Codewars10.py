# Task 1 Grasshopper - Summation

def summation(num):
    """
    Sum of all numbers before typed,
    including it
    """
    number = 0
    for i in range(num+1):
        number += i
    return print(number)


# summation(8)

# Task 2 Fix the loop!

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


# Task 3 Double Char

def double_char(s):
    new = ""
    for i in s:
        new += i*2
    print(new)


# liked
# def double_char(s):
#     return ''.join(c * 2 for c in s)

