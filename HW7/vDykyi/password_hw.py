import re

user_input = input("enter password: ")

while True:
    if len(user_input) < 6 and len(user_input > 16):
        print("wrong")
        break
    elif not re.findall("[a-z]", user_input):
        break
    elif not re.findall("[0-9]", user_input):
        break
    elif not re.findall("[$#@]", user_input):
        break
    elif not re.findall("[A-Z]", user_input):
        break
    else:
        print("Right password, hello")
        break
