# ----------1. In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

print('Even numbers that are divisible by 2:')
for num in range(1, 11):
    
    if num % 2 == 0:
        print(num)
print()

print('Odd numbers, which are divisible by 3:')
for num2 in range(1, 11):
    if num2 % 3 == 0:
        print(num2)
print()

print('Numbers that are not divisible by 2 and 3:')
for num3 in range(1, 11):
    if num3 % 2 != 0 and num3 % 3 != 0:
        print(num3)
print()
        