
my_range_list = [item for item in range(1,11)]

even_numbers, odd_numbers_dev_by_3, nither = [], [], []

for item in my_range_list:
    if item % 2 == 0:
        even_numbers.append(item)
    elif item % 3 == 0:
        odd_numbers_dev_by_3.append(item)
    elif item % 2 != 0 and item % 3 != 0:
        nither.append(item)

print(f'Even numbers that are devisible by 2 in the range from 1 to 10 are: {even_numbers}')

print(f'Odd numbers that are devisible by 3 in the range from 1 to 10 are: {odd_numbers_dev_by_3}')

print(f"Nnumbers that aren't devisible by 2 and 3 in the range from 1 to 10 are: {nither}")
