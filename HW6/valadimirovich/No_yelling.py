

def filter_words(st:str):
    
    """
    Function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
    String would be capitalized and properly spaced, without using re and string.
    """
    
    st = ' '.join((st.capitalize()).split())
    
    print(st)
    
    return st

