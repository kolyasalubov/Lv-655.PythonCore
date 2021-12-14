def count_sheeps(sheep):
    count = 0
    for item in sheep:
        if item == True:
            count += 1
        else:
            continue
    return count
