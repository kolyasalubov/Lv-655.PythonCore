from random import randint
import re
# Task 1 Script Game (random number)

# def guess_number():
#     """
#     Function to guess a number
#     """
#     rand_number = randint(1,100)
#     user_number = 0
#     while  user_number != rand_number:
#         user_number = int(input("Please chose a number: "))
#         if user_number> rand_number:
#             print("You number bigger than a randon, try again")
#             user_number = user_number
#         elif user_number < rand_number:
#             print("You number smaller than a randon, try again")
#             user_number = user_number
#         else:
#             print(f'You won, random number is {rand_number}')
#     return rand_number

# guess_number()

# Task 2 Validity of a password
def check_user_password():
    """
    Function to check user password
    """
    user_pass = input("Type your password: ")
    if re.findall("[a-z]", user_pass) != [] and re.findall("[A-Z]", user_pass) != [] and re.findall("[0-9]", user_pass) != [] and re.findall("[@#$]", user_pass) != [] and 6<len(user_pass)<16:
        print("Correct password!")
    else:
        print("Incorrect password")

check_user_password()
