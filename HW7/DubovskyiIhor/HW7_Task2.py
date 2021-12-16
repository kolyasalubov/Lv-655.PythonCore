# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import string

def validity(password):
    if len(password)>=6 or len(password)<=16:
        for item in password:
            if item in string.digits:
                result='valid'
            if item in string.ascii_lowercase:
                result='valid'
            if item in string.ascii_uppercase:
                result='valid'
            if item in string.punctuation:
                result='valid'
            else:
                result='invalid'
                      
    return result

print(validity(input('Input your password: ')))
