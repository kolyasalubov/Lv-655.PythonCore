

def count_positives_sum_negatives(arr) -> list:
    
    '''
    Function expects arrey of integers, and returns an array, 
    where the first element is the count of positives numbers 
    and the second element is sum of negative numbers.
    If the input array is empty or null, return an empty array. 
    Example
    For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], 
    return is [10, -65].
    '''
    
    if arr == [] or arr == [None] or arr == None:
        return arr
    
    counter_of_positive, sum_of_negative = 0 , 0
    
    for item in arr:
        
        if item > 0:
            counter_of_positive+=1
            
        elif item<0:
            sum_of_negative+=(item)
        
    return [counter_of_positive, sum_of_negative]

