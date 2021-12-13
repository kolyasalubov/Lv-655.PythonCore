# this is list of intergers
list_of_numbers = [1, 4, 6, 12, 4353, 534, 5345, 654645, 2]

# print initial data
print("\nInitial data")
print("List of intergers ", list_of_numbers)
print(type(list_of_numbers[0]))

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = float(list_of_numbers[i])

# print result data
print("\nResult data")
print("List of floats ", list_of_numbers)
print(type(list_of_numbers[0]))


