n=int(input('Input n: '))
fibonacci_list=[0]
f1=1
f2=1

while f1 <=n:
    fibonacci_list.append(f1)
    f1+=f2
    f1,f2=f2,f1

print(fibonacci_list)


