# Consider an array/list of sheep where some sheep may be 
# missing from their place. We need a function that counts 
# the number of sheep present in the array (true means 
# present).

def count_sheeps(sheep):
    sheep_count = 0
    for el in sheep:
        if el:
            sheep_count += 1
    return sheep_count
    