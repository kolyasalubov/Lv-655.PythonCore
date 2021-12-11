import re

user_password =re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#%$&8])[0-9a-zA-Z-!@#%$&8]{6,16}$')

val="""Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""

print(val)
if bool(user_password.match(input("enter yor pasword: ")))==True:
    print("Password meets the requirements")
else:
    print ("INVALID PASSWORD")
    print(val)
