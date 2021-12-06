def char_frequency(str):
    frequencies = {}
    for char in str:
        if char in frequencies:
            frequencies[char] +=1
        else:
            frequencies[char] = 1
    return frequencies

str = input("Write something: ")
print(f"Per char frequency in '{str}'' is:\n {char_frequency(str)}")