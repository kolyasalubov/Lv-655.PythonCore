# Write a Python program to check the validity of a 
# password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between 
# [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


user_password = input('Enter your password: ')

import re
def check_password(pattern):
    letters_valid_small = re.search('[a-z]', user_password)
    letters_valid_big = re.search('[A-Z]', user_password)
    numbers_valid = re.search('[0-9]', user_password)
    symbols_valid = re.search('[$#@]', user_password)
    length = len(user_password)

    return 'Your password is valid!' if letters_valid_small and letters_valid_big and numbers_valid and symbols_valid and length >= 6 and length <= 16 else 'Your password is invalid!'
