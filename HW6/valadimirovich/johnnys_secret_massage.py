

def greet(name):
    
    '''
    Function that returns a greeting for a user. 
    However, she's in love with Johnny, and would like to greet him slightly different.
    So if name is Johnny, it returns Hello, my love!
    '''
    
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

