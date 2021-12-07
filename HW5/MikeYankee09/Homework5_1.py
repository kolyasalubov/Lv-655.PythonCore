even = []
odd = []
other = []

for x in range(1,11):
    if x%2==0:
       even.append(x)
print("Even numbers, that are divisible by 2, from 1 to 10 are:", even)

for x in range(1,11):
    if x % 3 == 0:
        odd.append(x)
print("Odd numbers, which are divisible by 3, from 1 to 10 are:", odd)

for x in range(1,11):
    if x % 2 !=0 and x % 3 !=0:
        other.append(x)
print("Numbers, that are not divisible by 2 and 3, from 1 to 10 are:", other)
