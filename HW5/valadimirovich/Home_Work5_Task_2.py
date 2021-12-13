
validation = False


while not validation:
    validation = True if input('Please enter your login: ') == "First" else print('Please try again (Hint: login is case sensitive)')

    # Equvivalent of the code: 
    # 
    # if  input('Please enter your login: ') == "First":
    #     validation = True
    # else:
    #     print('Please try again (Hint: login is case sensitive)')

