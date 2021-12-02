a = int(input("Enter number: "))

factorial = 1
for i in range(a, 0, -1):
    factorial *= i

print("Factorial for {} is {}".format(a, factorial))