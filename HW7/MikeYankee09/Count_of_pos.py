'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
0 is neither positive nor negative.

If the input array is empty or null, return an empty array.
'''
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []