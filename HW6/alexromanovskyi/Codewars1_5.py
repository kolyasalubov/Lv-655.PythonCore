#Task_5
#You need to write a function that reverses the words in a given string. 
# A word can also fit an empty string.

def reverse(st):
    list=st.split()
    list.reverse()
    return ' '.join(list)

print (reverse("Whats up dude"))