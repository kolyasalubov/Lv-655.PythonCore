
x = int(input("Add a number of level:"))
fibo1 = 0
fibo2 = 1
fibo_next = 0
count = 0
if x <= 0 :
    print("Please enter a positive number")
elif x == 1:
    print(fibo1)
else:
    print("Fibonacci sequirence up to", x, "level")
    while count < x :
        print(fibo1)
        fibo_next = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo_next
        count += 1
