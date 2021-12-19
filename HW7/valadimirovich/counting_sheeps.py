

def count_sheeps(sheep) -> int:
    
    '''
    Function expects an array/list of sheep where some sheep may be missing from their place. 
    And counts the number of sheep present in the array (true means present).
    For example:
    [True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]

    The correct answer would be 17.
    Also checks for bad values like null/undefined
    '''
    
    counter = 0
    
    for item in sheep:
        
        if item == True:
            
            counter += 1
            
    return counter

