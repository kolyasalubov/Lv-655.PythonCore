first = input("Please input first value: ")
second = input("Please input second value: ")

print(f"First value: {first}. Second value: {second}")
first, second = second, first
print(f"First value: {first}. Second value: {second}")