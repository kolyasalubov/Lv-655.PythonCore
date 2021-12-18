

def reverse(st:str):
    
    '''
    Function expect string, reverses the words in it. 
    A word can also fit an empty string, input may have trailing spaces, 
    function ignore unneccesary whitespace. 
    Example (Input --> Output)
    "Hello World" --> "World Hello"
    "Hi There." --> "There. Hi"
    '''
    
    st = st.split()
    st.reverse()
    st = " ".join(st)

    return st

