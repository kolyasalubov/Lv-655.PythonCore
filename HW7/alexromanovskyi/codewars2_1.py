def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    countpos=0
    sumofneg=0
    for numbers in arr:
        if numbers<0:    
            sumofneg+=numbers
        if numbers>0:
            countpos+=1
            
    return [countpos,sumofneg]