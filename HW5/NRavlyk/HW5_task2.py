# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

repeat = True
while repeat:
    user_login = input("Please input login: ")
    if user_login=="First":
        print("Greeting you")
        repeat =False
    else:
        print("Please enter a valid login")
