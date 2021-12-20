# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
#arr=[]

#sum(x for x in a if x<0)

def count_positives_sum_negatives(arr):
    if arr==[]:
        return []
    return [len(list(x for x in arr if x>0)),sum(x for x in arr if x<0)]
print(count_positives_sum_negatives(arr))