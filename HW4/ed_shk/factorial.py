# calculate factorial for positive intergers
try:
    y = int(input("Enter some positive interger "))
    factorial = 1
    if y == 0:
        print("Factorial of {a} is {b}".format(a = y, b = factorial))
    elif y > 0:
        counter = y
        while counter > 0:
            factorial = factorial * counter
            counter = counter - 1
        print("Factorial of {a} is {b}".format(a = y, b = factorial))
    else:
        print("Factorial is not existed (*)")
except ValueError:
    print("Only positive interger numbers accepted")
