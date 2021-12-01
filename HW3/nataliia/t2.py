num = 5374
a = num % 10
num = num //10
b = num % 10
num = num //10
c = num % 10
num = num //10
d = num % 10
print("multiplication = ",a*b*c*d)
print(a,b,c,d)
num_1 = []
num_1.append(a)
num_1.append(b)
num_1.append(c)
num_1.append(d)
print(sorted(num_1))