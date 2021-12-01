f2 = f1 = 1 

n = int(input("Введіть чило межу послідовності"))

print(f2, end=' ')
while f2 < n:
    print(f2, end=' ')
    f1 , f2 = f2 , f1 + f2