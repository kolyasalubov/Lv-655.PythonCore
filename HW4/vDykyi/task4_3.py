#task4_3
num1 = 0
num2 = 1

fibonachhi = int(input("Enter number: "))

while num2 < fibonachhi:
    print(num1)
    num1, num2 = num2, num1 + num2
    