#Given an array of integers.
# Return an array, where the first element is 
# the count of positives numbers and the second 
# element is sum of negative numbers.
# If the input array is empty or null, return an 
# empty array.

def count_positives_sum_negatives(arr):
    if not arr: return []
    positives_count = 0
    negatives_sum = 0
    for num in arr:
        if num > 0:
            positives_count += 1
        else:
            negatives_sum += num
    return [positives_count, negatives_sum]
