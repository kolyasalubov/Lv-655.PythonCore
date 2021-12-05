# Task3. Write a function that calculates the number of characters included in a given string

def char_number():
    string = input('Enter a string: ')
    string_without_spaces = string.replace(" ", "")
    print('The number of characters in a string: ', len(string_without_spaces))

char_number()


# Option using one more variable

# def char_number():
#     string = input('Enter a string: ')
#     string_without_spaces = string.replace(" ", "")
#     string_length = len(string_without_spaces)
#     print(string_length)

# char_number()

# My drafts

# for fruit in ['apple','banana','mango']:    
# 	print("I like",fruit)

# print(sorted(a))
# print(a.union())
# a.union.pop()
# print(a)
# def aa():
#     enumerate(a)
# print(aa)
# print(type(a))
# print(a)
# print(a[0])
# print(a.count('w'))
# print(enumerate(a))

# x = ['apple', 'banana', 'cherry']
# y = enumerate(x)
# print(list(y))
