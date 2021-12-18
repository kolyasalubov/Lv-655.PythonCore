user_name = input('What is your name? ')

try:
    user_age = int(input('How old are you? '))
except:
    print('Pleas ininteger number for the age: ')

    try:
        user_age = int(input('How old are you? '))
    except:
        print('Please try to input integer for the age next time, script would be terminated now, bye')
        exit()

user_location = input('Where do you live? ')

print(f'Hello,{user_name}')

print(f'Your age is {user_age}')

print(f'You live in {user_location}')
