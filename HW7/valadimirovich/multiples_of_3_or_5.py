

def solution(number) -> int:
    
    '''
    Function expects intager atribute and returns the sum of all the multiples 
    of 3 or 5 below the number passed in. 
    Additionally, if the number is negative, return 0.
    Note: If the number is a multiple of both 3 and 5, it only count it once.
    '''
    
    result = 0
    
    if number <= 0:
        
        return result 
    
    else:
        
        for numbers in range(number):
            
            if numbers % 3 == 0 or numbers % 5 == 0:
                
                result += numbers
                
    return result

  