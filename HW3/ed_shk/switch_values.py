# switch values without intermediate storage
first_value = input("Give me first value: ")
second_value = input("Give me second value: ")

first_value, second_value = second_value, first_value

print("\nNow first value is: ", first_value)
print("and second value is: ", second_value)
