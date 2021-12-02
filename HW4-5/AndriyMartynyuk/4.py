# Task 1 Factorial

factorial = 0
while factorial == 0:
    try:
        factorial = int(input("Put a number to calculate factorial: "))
        factorial_result = 1
        for i in range(factorial):
            i += 1
            factorial_result *= i
    except ValueError:
        print("Please, use a number!")
        factorial = 0
        continue
    print(factorial_result)

# Task 2 integer - float

list_of_numbers = []
amount_of_numbers = 0
i = 0
numbers = 0
counter = 1
while amount_of_numbers == 0:
    try:
        amount_of_numbers = int(
            input("How many numbers you want to have in your list?"))
        if amount_of_numbers < 0:
            print("You can't use a negative value. Please change to a positive!")
            amount_of_numbers = 0
            continue
        while numbers == 0:
            try:
                while i < amount_of_numbers:
                    print("Type a number", counter, ": ")
                    numbers = input()
                    list_of_numbers.append(float(numbers))
                    i += 1
                    counter += 1
            except ValueError:
                print("Please, use a number!")
                numbers = 0
        print("This is your float list:", list_of_numbers)
    except ValueError:
        print("Please, use a Number!")
        amount_of_numbers = 0


# Task 3 Fibonachi
# first option - show fibonachi numbers less then user type
number = 0
while number == 0:
    try:
        number = int(input("Please, put some number: "))
        if number < 0:
            print("You can't use a negative value. Please change to a positive!")
            number = 0
            continue
        f = 0
        f_1 = 1
        f_2 = 1
        print(f)
        while f_2 < number:
            print(f_2)
            f_2 = f_1 + f
            f = f_1
            f_1 = f_2
    except ValueError:
        print("Please, use a number!")
        number = 0

# second option - show how many Fibonachi numbers user want to see
n = 0
while n == 0:
    try:
        n = int(input("How many Fibonachi numbers you want to see? "))
        if n < 0:
            print("You can't use a negative value. Please change to a positive!")
            n = 0
            continue
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
    except:
        print("Please, use a number!")
        n = 0
