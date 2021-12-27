# Task3. Write a function that calculates the number of 
# characters included in a given string
# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}

def calculate_characters(word):
    result = {}
    for item in word:
        if item in result:
            continue
        else:
            result.update({str(item): word.count(item)})
    return result

print(calculate_characters('hello'))
