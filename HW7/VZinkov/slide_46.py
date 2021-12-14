# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$  # @].
# Minimum length 6 characters.
# Maximum length 16 characters.
import re

password = input()

# if len(password) < 6:
#     print('Password should have 6 characters or more')
# elif len(password) > 16:
#     print('Password should not be longer than 16 characters')
# elif re.search(r'[!-@]', password) == None:
#     print('Password shoud contain symbols')
# elif re.search(r'[0-9]', password) == None:
#     print('Password should contain at least one number')
# elif re.search(r'[a-z]', password) == None:
#     print('Password should contain at least 1 small letter')
# elif re.search(r'[A-Z]', password) == None:
#     print('Password should contain at least 1 big letter')
# else:
#     print('You are welcome')


print('You are wrong') if len(password) < 6 or len(password) > 16 or re.search(r'[!-@]', password) == None or re.search(
    r'[0-9]', password) == None or re.search(r'[a-z]', password) == None or re.search(r'[A-Z]', password) == None else print('Hello')
