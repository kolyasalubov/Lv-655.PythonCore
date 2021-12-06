login = ''
while login != 'First':
    login = input("Please loggin in the system: ")
    if login == 'First':
        break
    else:
        print("Something went wrong, please try again")
print("Welcome to the system!")