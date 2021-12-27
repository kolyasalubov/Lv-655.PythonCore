# Create a function which answers the question 
# "Are you playing banjo?".
# If your name starts with the letter "R" or lower case 
# "r", you are playing banjo!
# The function takes a name as its only argument, and 
# returns one of the following strings:

def are_you_playing_banjo(name):
    
    # return f'{name} plays banjo' if name.startswith('r') or name.startswith('R') else f'{name} does not play banjo'

    return f'{name} plays banjo' if name[0] == 'r' or name[0] == 'R' else f'{name} does not play banjo'
