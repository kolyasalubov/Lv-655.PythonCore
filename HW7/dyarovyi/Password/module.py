uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghihjklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "$#@"

def check_validity(password):
    contains_upper = False
    contains_lower = False
    contains_numbers = False
    contains_symbols = False

    for char in password:
        if char  in lowercase_letters:
            contains_lower = True
        elif char in uppercase_letters:
            contains_upper = True
        elif char in numbers:
            contains_numbers = True
        elif char in symbols:
            contains_symbols = True
    
    return contains_upper and contains_lower and contains_numbers and contains_symbols

if __name__ == "__main__":
    password = input("Enter password: ")
    print("The password is {}".format("valid" if check_validity(password) else "invalid"))