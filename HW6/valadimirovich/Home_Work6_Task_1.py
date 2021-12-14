

def compering_two_numbers(first_number=0, second_number=0):
    
    '''
    Function returns the largest number of two numbers
    '''

    if first_number > second_number:
        return first_number
    elif first_number == second_number:
        print("Numbers are equal, so I'll return first one")
        return first_number
    else: 
        return second_number

