# In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

x = []
y = []
z = []
for item in range (1, 11):
    if item%2==0:
        x.append(item)
    elif item%3==0:
        y.append(item)
    else: 
        z.append(item)
print(x, "numbers that are divisible by 2")
print(y, "numbers, which are divisible by 3")
print(z, "numbers that are not divisible by 2 and 3")