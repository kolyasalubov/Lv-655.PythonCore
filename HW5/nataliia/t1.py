even_num = [x for x in range (1, 11) if x % 2 == 0]
print(even_num)
odd_num = [y for y in range (1, 11) if y % 3 == 0]
print(odd_num)
other_num = [z for z in range (1, 11) if z % 2 != 0 and z % 3 != 0]
print(other_num)