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
            if item in [$#@]:
                result='valid'
            else:
                result='invalid'
                      
    return result

print(validity(input('Input your password: ')))

###################################################################


import re

def validity():
    result_1 = re.findall("[a-z]", pattern)
    result_2 = re.findall("[A-Z]", pattern)
    result_3 = re.findall("[$#@]", pattern)
    result_4 = re.findall("\d", pattern)
    if bool(result_1)==True and bool(result_2)==True and bool(result_3)==True and bool(result_4)==True:
        return("Valid password")
    else:
        return("Invalid password")   

pattern=input('Input your password: ')
if len(pattern)>=6 and len(pattern)<=16:
    print(validity())
else:  
    print("Invalid password")

  



