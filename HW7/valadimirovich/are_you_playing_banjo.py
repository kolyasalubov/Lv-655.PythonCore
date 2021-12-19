

def are_you_playing_banjo(name) -> str:

    '''
    The function takes a name as its only argument, and returns one of the following strings:
    name + " plays banjo" - If name starts with 'R' or 'r'
    name + " does not play banjo" - If it starts from any other character
    Names given are always valid strings.
    '''
    
    if name[0] == 'R' or name[0] == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'

