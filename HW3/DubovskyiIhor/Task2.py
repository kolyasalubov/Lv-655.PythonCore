n=int(input('Input: '))
l=str(n)
reversed=l[::-1]
mult=1
while n!=0:
    a=n%10
    mult*=a
    n=n//10
print(mult)

print(reversed)
print(sorted(l))