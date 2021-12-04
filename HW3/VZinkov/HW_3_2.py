a=int(input("Enter your 4-digit number:"))
b=a/1000
c=a/100%10
d=a/10%10
e=a%10
print(b*c*d*e)

g=str(a) [::-1]
print(g)

asc  = "".join(sorted(str(a)))
desc = "".join(sorted(str(a), reverse=True))

print (asc)
print (desc)
