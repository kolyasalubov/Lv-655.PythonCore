# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

login = input("Your name: ")

while login != "First":
    print ("Wrong login, try again!")
    login = input("Your name: ")
else: print ("Welcome!")