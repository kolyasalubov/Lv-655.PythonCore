

def correct_tail(body, tail) -> bool:
    
    '''
    Function expects for two string arguments the second argument (tail), 
    is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
    If the tail is right return true, else return false.
    The arguments will always be strings, and normal letters.
    '''
    
    if body[-1] == tail:                     
        return True
    else:
        return False

