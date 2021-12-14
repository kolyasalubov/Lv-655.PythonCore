def get_number_or_chars(string):
    dict_chars = {}

    for c in string:
        if not c in dict_chars.keys():
            dict_chars[c] = 1
        else:
            dict_chars[c] += 1

    return dict_chars


string = input("Enter string: ")
print(get_number_or_chars(string))