import re


def are_you_playing_banjo(name):
    if re.match(r'R', name) or re.match(r'r', name):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
