n = int(input("Enter n: "))

a = 0
b = 1

while a < n:
    print(a)

    if b < n:
        print(b)
        
    a += b
    b += a