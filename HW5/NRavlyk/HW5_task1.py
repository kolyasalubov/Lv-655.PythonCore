even_numbers = []
odd_numbers_non_3 =[]
not_divisible_2_3 =[]

for n in range(1,10):
    even_numbers.append(n) if n%2==0 else None
    odd_numbers_non_3.append(n) if n%2==1 and n%3==0 else None
    not_divisible_2_3.append(n) if n%2 != 0 and n%3 != 0 else None

print("even numbers that are divisible by 2: ", even_numbers)
print("odd numbers, which are divisible by 3: ", odd_numbers_non_3)
print("numbers that are not divisible by 2 and 3: ", not_divisible_2_3)

