import re

password = str(input("Add password: "))

if 6>(len(password))<16:
    print ("Minimum length must have 6 characters")
elif not re.findall(r'[az]', password):
    print ("Password must contain at least one a-z")
elif not re.findall(r'[AZ]', password):
    print ("Password must contain at least one A-Z")
elif not re.findall(r'\d', password):
    print ("Password must contain at least one 0-9")
elif not re.findall('[$#@]', password):
    print ("Password must contain at least one $#@")
else:
    print ("Good password !")