# ----------2. Write a script that checks the login that 
# the user enters. 
# If the login is "First", then greet the users. If the 
# login is different, send an error message. 
# (need to use loop while)

while True:
    user_input = input('Enter your login: ')
    if user_input == 'First':
        print('Hello, user!')
    else:
        print('Error! Try again')
