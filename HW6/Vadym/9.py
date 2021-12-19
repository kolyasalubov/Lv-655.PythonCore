# Write a function that calculates the number of characters included in a given string

# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}

def count_charters (str):
    """
    function that calculates the number of characters included in a given string
    input: “hello”
    output: {“h”:1, “e”:1, “l”:2, “o”:1}"""
    return {a: str.count(a) for a in str}

print(count_charters("Motobat"))
