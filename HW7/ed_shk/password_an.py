# check if user's password match our prerequsites
import re

def checklen(password):
    """
    Check if password have acceptable length 6-16 characters
    input: string
    output: boolean
    """
    return False if len(password) < 6 or len(password) > 16 else True 

def check_letters(password):
    """
    Check if passoword includes at least 1 letter between 'a and z' and 1 letter between 'A and Z'
    input: string
    output: boolean
    """
    return True if re.findall("[a-z]", password) and re.findall("[A-Z]", password) else False  

def check_digits_specs(password):
    """
    Check if passoword includes at least 1 digit and 1 of special symbols $ @ #'
    input: string
    output: boolean
    """
    return True if re.findall("\d", password) and re.findall("[$@#]", password) else False

password = input("Please enter your password: ")
if checklen(password):
    if check_letters(password) and check_digits_specs(password):
        print("Your password as strong as Hercules!")
    else:
        print("You password is not too strong")
else:
    print("Length of your password is not acceptable")
