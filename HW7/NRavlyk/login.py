
# import re

# good_pass = False
# while not good_pass:
#     user_pass = input("please input valid password ")

#     # pattern = re.compile(r'(?:[A-Z]|[a-z]|\d|[$#@])')
#     # listm= pattern.findall(user_pass) 
#     # print (listm)

#     pas_small_letters=len(re.findall(r'[a-z]',user_pass))
#     pas_big_letters=len(re.findall(r'[A-Z]',user_pass))
#     pas_numbers  = len(re.findall(r'\d',user_pass))
#     pas_sym = len(re.findall(r'[$#@]',user_pass))
#     other_sym = len(re.findall(r'[^A-Za-z\d$#@]',user_pass))
    

#     if (pas_small_letters and 
#         pas_big_letters == 1 and 
#         pas_numbers and 
#         pas_sym and 
#         not other_sym and
#         6<pas_small_letters+pas_big_letters+pas_numbers+pas_sym<16):
        
#         good_pass=True
# print("You password is good")


import re

good_pass = False
while not good_pass:
    user_pass = input("please input valid password ")

    if (len(re.findall(r'[A-Z]',user_pass))==1 and 
        re.findall(r'[a-z]',user_pass) and 
        re.findall(r'\d',user_pass) and 
        re.findall(r'[$#@]',user_pass) and 
        not re.findall(r'[^A-Za-z\d$#@]',user_pass) and
        6<len(re.findall(r'[A-Za-z\d$#@]',user_pass))<16): 


        good_pass=True

print("You password is good")