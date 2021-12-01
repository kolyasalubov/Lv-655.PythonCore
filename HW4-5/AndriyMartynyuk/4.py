# Task 1 Factorial

factorial = int(input("Put a number to calculate factorial: "))
factorial_result = 1
for i in range(factorial):
    i += 1
    factorial_result *= i

print(factorial_result)

# Task 2 integer - float

list_of_numbers = []
i = 0
amount_of_numbers = int(
    input("How many numbers you want to have in your list?"))
while i < amount_of_numbers:
    numbers = input("Type a number: ")
    list_of_numbers.append(float(numbers))
    i += 1
print("This is your float list:", list_of_numbers)


# Task 3 Fibonachi
# first option - show fibonachi numbers less then user type

number = int(input("Please, put some number: "))
f = 0
f_1 = 1
f_2 = 1
print(f)
while f_2 < number:
    print(f_2)
    f_2 = f_1 + f
    f = f_1
    f_1 = f_2

# second option - show how many Fibonachi numbers user want to see

n = int(input("How many Fibonachi numbers you want to see? "))
f = 0
f_1 = 1
f_2 = 1
print(f)
i = 0
while i < (n-1):
    print(f_2)
    f_2 = f_1 + f
    f = f_1
    f_1 = f_2
    i += 1
