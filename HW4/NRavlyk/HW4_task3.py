number = 0
while True:
    number_str = input("Please input number > 0  : ")
    try:
        number = int (number_str)
        if number > 0:
            break         
    except:
        print("Once more")

x1,x2=0,1
print (x1, end=" ")
while x2<number:
    x1 +=x2
    x1, x2 = x2, x1
    print (x1, end=" ")