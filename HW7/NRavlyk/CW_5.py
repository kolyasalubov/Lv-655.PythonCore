def are_you_playing_banjo(name):
    if name[0]=='R' or name[0]=='r':
        name +=" plays banjo" 
    else:
        name +=" does not play banjo"
    #  Implement me!
    return name


# NOT MY

# def areYouPlayingBanjo(name):
#    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

# def areYouPlayingBanjo(name):
#     return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"