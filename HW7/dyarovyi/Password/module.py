import re as re

uppercase_letters = "[A-Z]"
lowercase_letters = "[a-z]"
numbers = "\d"
symbols = "[$#@]"

def check_validity(password):
    contains_upper = False
    contains_lower = False
    contains_numbers = False
    contains_symbols = False

    if re.findall(uppercase_letters, password) != None:
        print(re.findall(uppercase_letters, password))
        contains_lower = True
    if re.findall(lowercase_letters, password) != None:
        print(re.findall(lowercase_letters, password))
        contains_upper = True
    if re.findall(numbers, password) != None:
        print(re.findall(numbers, password))
        contains_numbers = True
    if re.findall(symbols, password) != None:
        print(re.findall(symbols, password))
        contains_symbols = True
    
    return contains_upper and contains_lower and contains_numbers and contains_symbols and (6 <= len(password) <= 16)

if __name__ == "__main__":
    password = input("Enter password: ")
    print("The password is {}".format("valid" if check_validity(password) else "invalid"))