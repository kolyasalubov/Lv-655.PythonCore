import re

#Too complicted and looks stupid but, at least it does work, however I'm shamed by just looking at it

invalid = True

while invalid:
    
    # if re.findall(r'[a-z]', user_pass) != [] \
    #     and re.findall(r'[A-Z]', user_pass)!=[] \
    #     and re.findall([#@$], user_pass)!=[] \
    #     and re.findall(r'[0-9]', user_pass)!=[] \
    #     and 6 < len(user_pass) < 16:
    #     invalid = False

    # # And it could be as simple as that:
    user_pass = input("Please create your pasword: ")
    
    if re.findall("(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[@#$])[a-zA-Z/\d@#$]{6,16}", user_pass):
            invalid = False
    

print('You did it, you son of a gun!')

