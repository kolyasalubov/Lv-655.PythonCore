a=int(input("Обчислити факторіал числа: "))
f=1
if a>=0:  
    while a!=0:
          f*=a
          a-=1
    print(f)      
else:
    print("error") 