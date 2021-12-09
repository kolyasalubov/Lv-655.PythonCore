def characters(string):
    
    """"function that calculates the number of characters included in a given string"""
 
    str = {}
    for letter in string:
        if letter in str:
            str[letter] +=1
        else: 
            str[letter] =1
    return str

string = input("Add word: ")
print(characters(string))

