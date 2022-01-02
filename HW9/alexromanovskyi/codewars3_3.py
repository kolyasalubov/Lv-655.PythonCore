def double_char(s):
    output = []
    for char in s:
        output.append(char+""+char)
    return "".join(output)