

def calculating_string_chars(input_string:str):

    '''
    Function expects string, calculates the number of characters included in a given string
    Returns dict
    Example: 
    input: “hello”
    output: {“h”:1, “e”:1, “l”:2, “o”:1}
    '''

    result = {}

    for character in input_string:

        result.update({character : input_string.count(character)})

    return result

