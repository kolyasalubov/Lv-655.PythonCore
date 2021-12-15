def summation(num):
    numbers = []
    for item in range(0, num):
        item += 1
        numbers.append(item)

    return sum(numbers)


print(summation(8))
