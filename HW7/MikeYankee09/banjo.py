'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
'''


def are_you_playing_banjo(name):
    if name[0] == 'r' or name[0] == 'R':
        return f"{name} plays banjo"
    return f"{name} does not play banjo"