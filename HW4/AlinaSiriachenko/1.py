# Task1. Write a script that will calculate the factorial 
# of the entered number  without using recursion.

number = int(input('Enter a number: '))
factorial = 1
if number < 0:
    print('Cannot accept negative numbers.')
elif number == 0:
    print('Factorial of 0 is 1')
else:
    for el in range(1, number + 1):
        factorial = factorial * el
    print(f'Factorial of {number} is {factorial}')
    