def count_sheeps(array):
    count = 0
    for sheep in array:
        if sheep:
            count += 1
    return count