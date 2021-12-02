# print numbers under given conditions
range_of_numbers = 10

print("\nIn range from 1 to {a}".format(a = range_of_numbers))
# even numbers divisible by 2
print("Even numbers divisible by 2 are {b}".format(b = [x for x in range(range_of_numbers + 1) if x % 2 == 0]))

#odd numbers divisible by 3
print("Odd numbers divisible by 3 are {c}".format(c = [x for x in range(range_of_numbers + 1) if x % 2 != 0 and x % 3 == 0]))

#numers_not divisible by 2 and 3
print("Numbres not divisible by 2 and 3 are {d}".format(d = [x for x in range(range_of_numbers + 1) if x % 2 != 0 and x % 3 != 0]))
