# Naive conversation program

user_name = ''
user_age = ''
user_location = ''

# wait for users name, age and location
while user_name == '':
    user_name = input('What is your name? ')

while user_age == '' or user_age.isnumeric() == False:
    user_age = input('How old are you? ')

while user_location == '':
    user_location = input('Where do you live? ')

# Give some conversation based on information provided by user
print('Hello,', user_name)
print('Your age is:', user_age)
print('You live in:', user_location)
