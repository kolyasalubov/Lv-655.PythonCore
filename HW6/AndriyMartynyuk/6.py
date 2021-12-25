# Task 1

print("Even numbers that are divisible by 2:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("Odd numbers, which are divisible by 3:")
for i in range(1, 11):
    if i % 2 != 0 and i % 3 == 0:
        print(i)

print("Numbers that are not divisible by 2 and 3:")
for i in range(1, 11):
    if i % 2 != 0 and i % 3 != 0:
        print(i)

# Task 2
users_login = ""
while users_login == "":
    users_login = input("Please, write your login: ")
    if users_login == "First":
        print("Hello,", users_login)
    else:
        print("Your login isn't  correct, please check it")
        users_login = ""
