# Task1. In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

print([i for i in range(1,11)])       
print([i for i in range(1,11) if i%2 == 0])
print([i for i in range(1,11) if i%2!= 0 and i%3==0])
print([i for i in range(1,11) if i%2!= 0 and i%3!=0])
