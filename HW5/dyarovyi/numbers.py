divisible_by_2 = []
divisible_by_3 = []
divisible_by_2_3 = []

for i in range(10):
    if not i % 2:
        divisible_by_2.append(i)
    if i % 3 == 0:
        divisible_by_3.append(i)
    if i % 2 != 0 and i % 3 != 0:
        divisible_by_2_3.append(i)

print("Divisible by 2:", divisible_by_2)
print("Divisible by 3:", divisible_by_3)
print("Divisible by 2 and 3:", divisible_by_2_3)