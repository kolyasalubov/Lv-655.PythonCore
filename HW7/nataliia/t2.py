import re

password = str(input("Enter a password: "))

if not re.findall("[a-z]", password):
    print("Password should have at least 1 small letter.")
elif not re.findall("[A-Z]", password):
    print("Password should have at least 1 big letter.")
elif not re.findall("\d", password):
    print("Password should have at least 1 number.")
elif not re.findall("[$#@]", password):
    print("Password should have at least 1 character from $#@.")
elif not re.findall("^.{6,16}$", password):
    print("Password should have more than 6 characters and less than 16 characters.")
else:
    print("Your password is strong")
    