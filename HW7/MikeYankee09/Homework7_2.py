
import re

password = str (input ("Please input a password: "))

if not re.findall ('[a-z]', password):
    print ("At least 1 letter must be between [a-z]")
elif not re.findall ('[A-Z]', password):
    print ("At least 1 letter must be between [A-Z]")
elif not re.findall ('[0-9]', password):
    print ("At least 1 letter must be digit between[0-9]")
elif not re.findall ("[$#@]", password):
    print ("At least 1 character from [$#@]")
elif not 6 <= len(password) <= 16:
    print("Minimum length of password is 6 characters, max lenth is 16 characters")
else:
    print (password, "is strong enough")
    