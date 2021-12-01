# Task3. Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 
# 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

number = int(input('Enter a number: '))
fibo_number_0 = 0
fibo_number_1 = 1
count = 0
if number <= 0:
    print('Enter a positive number.')
elif number == 1:
    print('The Fibonacci sequence up to {number} is: ')
    print(f'{fibo_number_1}')
else:
    print('The Fibonacci sequence is: ')
    while count < number:
        print(fibo_number_0)
        new_fibo_number = fibo_number_0 + fibo_number_1
        fibo_number_0 = fibo_number_1
        fibo_number_1 = new_fibo_number
        count += 1
