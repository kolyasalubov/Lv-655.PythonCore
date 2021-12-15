def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    c_of_pos=0
    sum_neg=0
    for num in arr:
        if num>0:
            c_of_pos+=1
        if num<0:    
            sum_neg+=num
            
    return [c_of_pos,sum_neg]

 