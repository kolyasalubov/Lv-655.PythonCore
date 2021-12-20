

def list_animals(animals:list) -> str:
    '''
    Function expects list of the animals 
    forms and returns string with orderings and newlines sign added.
    
    For example, passing in:
    animals = [ 'dog', 'cat', 'elephant' ]
    will result in:
    list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
    '''
    
    string = ''
    i=1
    
    for animal in animals:
        
        string += str(i) + '. ' + str(animal) + '\n'
        i+=1
        
    return string

