#Factorial
#Write a script that will calculate the factorial of the entered number  without using recursion.

num = int(input("number: "))

factorial = 1

for y in range(1, num+1):
    factorial *= y

print (factorial)
