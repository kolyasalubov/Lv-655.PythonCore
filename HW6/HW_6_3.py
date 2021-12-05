def count(str1):
    """
    Counts how many repeated symbols you have in the world

    Parameters (str1) - your world
    """
    letters=list(str1)
    counts=dict()
    for letter in letters:
        counts[letter]=counts.get(letter,0)+1
    return counts

print (count('ababagalamaga'))
