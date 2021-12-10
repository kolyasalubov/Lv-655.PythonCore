# Task3. Write a function that calculates the number of characters included in a given string

# input: "hello"
# output: {"h":1, "e":1,"l":2,"o":1}

input_string=input("please input you word: ")

dicstr={}
for  letter in input_string:
    dicstr[letter]=dicstr.get(letter,0)+1

print(dicstr) 
