# claculate number of characters in string given by user 

def char_number(user_string):
    """
    input: string
    output: dictionary
    Calculate naumber of characters in string
    """
    result = {}
    for character in user_string:
        if character in result:
            result[character] = result[character] + 1
        else:
            result[character] = 1
    return result

user_string = input("Gimme some string: ")
result = char_number(user_string)
for character in result:
    print(character, result[character])

