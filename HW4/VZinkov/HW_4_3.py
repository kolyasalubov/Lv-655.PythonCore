a=int(input("Enter your number: "))

n1=0
n2=1
count=0

while count<a:
    print(count,n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1

