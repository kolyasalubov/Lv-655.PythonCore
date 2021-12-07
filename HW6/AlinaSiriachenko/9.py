# Task3. Write a function that calculates the number of 
# characters included in a given string
# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}

def calculate_characters(string):
    unique = []
    for letter in string:
        if letter not in unique:
            unique.append(letter)
    return len(unique)

print(calculate_characters('hello'))
