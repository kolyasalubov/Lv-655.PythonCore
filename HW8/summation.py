

def summation(num:int) -> int:
    '''
    Function expects integer number and returns the summation of every number from 1 to num. 
    The number should always be a positive integer greater than 0.
    For example:
    summation(2) -> 3
    1 + 2
    summation(8) -> 36
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
    '''
    
    result = 0
    for number in range(1,num+1):
        result+=number
    return result
    
