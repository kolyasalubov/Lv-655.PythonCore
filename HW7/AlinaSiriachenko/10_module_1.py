# Write a Python program to check the validity of a 
# password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between 
# [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# user_password = input('Enter your password: ')

def letters_a_z_A_Z(user_password):
    # lower_a_z = ['a', 'b', 'c', 'd', 'e', 
    #              'f','g', 'h', 'i', 'j', 'k',
    #              'l', 'm', 'n', 'o', 'p', 
    #              'q', 'r', 's', 't', 'u'
    #              'v', 'w', 'x', 'y', 'z']
    #     # lower_a_z = ['a', 'b', 'c', 'd'efghijklmnopqrstuvwxyz']

    # upper_a_z = ['A', 'B', 'C', 'D', 'E'
    #             'F', 'G', 'H', 'I', 'J', 'K',
    #             'L', 'M', 'N', 'O', 'P',
    #             'Q', 'R', 'S', 'T', 'U',
    #             'V', 'W', 'X', 'Y', 'Z']

        # upper_a_z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for el in user_password:
        if el in letters:
            return True
        else:
            return False

print(letters_a_z_A_Z('a'))

# def numbers(user_password):
#     nums = [num for num in range(0, 10)]
#     if user_password in nums:
#         return 
