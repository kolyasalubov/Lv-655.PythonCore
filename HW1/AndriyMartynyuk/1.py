# # Lesson 1 23.11.2021
# Home task
# 1. Create 3 questions throught "Input" and answer to iter
# 2. Practice with a math
# 3. Install Git client an GitHub (Done)


# 1 Task (questions)

# Question 1

# Варіант 1

user_name = ""
while user_name == "":
    user_name = input("What is your name?")
    if user_name == "":
        print("Please, type your name")
        user_name = ""
    count = 0
    for i in user_name:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            count += 1
            continue
    if count > 0:
        print("Please, use only letters")
        user_name = ""

print("Welcome,", user_name)

# Варіант 2

# user_name = ""
# while user_name == "":
#     user_name = input("What is our name?")
#     try:
#         if int(user_name) > -999999999999999999999999999999999:
#             print("Please, use a letter")
#             user_name = ""
#     except ValueError:
#         print("Hello,", user_name, type(user_name))

# Question 2
user_age = 0
while user_age == 0:
    try:
        user_age = int(input("How old are you?"))
        if user_age < 0:
            user_age = 0
            print("Please, type your current age")
        elif user_age > 0 and user_age < 18:
            print("You just starting your path. Welcome,", user_name, "!")
        else:
            print("Welcome,", user_name, "!")
    except ValueError:
        user_age = 0
        print("Please, put a number!")

# Question 3
user_email = ""
while user_email == "":
    user_email = input("Please, type your email")
    user_email_split = user_email.split("@")
    if len(user_email_split) > 1 and user_email_split[1] != "":
        user_email_split_second_part = user_email_split[1].split(".")
        if len(user_email_split_second_part) > 1 and user_email_split_second_part[1] != "":
            print("You email is", "'", user_email, "'", "Thank's!")
        else:
            print("Part after @ has to be with a '.', please check your dial")
            user_email = ""
    else:
        print("You dial a wrong email. Please, try again")
        user_email = ""

print("Hello, please check your information. Your name is:",
      user_name, "You age is:", user_age, "Your email is:", user_email)


# 2 Task (Math)

a = 6
b = 10
c = 2

print("a+b", a+b)
print("a*b", a*b)
print("a/b", a/b)
print("a*b", a*b)
print("a//b", a//b)
print("a%b", a % b)
print("a**b**c", a**b**c)
