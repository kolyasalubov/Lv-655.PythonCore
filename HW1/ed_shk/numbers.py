# Base operations with two numbers: +, -, *, /, **

# Welcome info
print('Please enter two numbers')

# Wait for two numbers from user
while True:
    try:
        a = float(input('First number A: '))
        break
    except ValueError:
        print('Only numbers acceptable. Use "." to separate decimal. Please, try again')

while True:
    try:
        b = float(input('Second number B: '))
        break
    except ValueError:
        print('Only numbers acceptable. Use "." to separate decimal. Please, try again')

# Print results
try:
    print('A - B = ', a - b)
    if b != 0:
        print('A / B = ', a / b)
        print('A // B = ', a // b)
    else:
        print('A / B Division by zero')
        print('A // B Division by zero')
    print('A + B = ', a + b)
    print('A * B = ', a * b)
    print('A ** B = ', a ** b)
except OverflowError:
    print("Numbers too big to complete all operations")
