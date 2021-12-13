def characters(input_string):
    
    """"function that calculates the number of characters included in a given string"""
 
    str = {}
    for letter in input_string:
        if letter in str:
            str[letter] +=1
        else: 
            str[letter] =1
    return str

input_string = input("Add word: ")
print(characters(input_string))

