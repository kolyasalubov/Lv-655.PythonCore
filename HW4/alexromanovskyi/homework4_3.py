# Print Fibonacci numbers up to the entered number n, 
# using cycles. 

a, b = 0, 1
n = int(input("Add your number: "))

if n<=b:
    print("Please change your number")
while n>b:
    print(b, end="")
    a,b = b, a+b
print()