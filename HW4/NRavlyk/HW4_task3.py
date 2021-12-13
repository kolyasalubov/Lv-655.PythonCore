number = 0
while True:
    number_str = input("Please input number > 0  : ")
    try:
        number = int (number_str)
        if number > 0:
            break         
    except:
        print("Once more")

Fibonacci,x2=0,1
print (Fibonacci, end=" ")
while x2<number:
    Fibonacci +=x2
    Fibonacci, x2 = x2, Fibonacci
    print (Fibonacci, end=" ")