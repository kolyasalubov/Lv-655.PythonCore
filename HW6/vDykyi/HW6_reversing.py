#Reversing Words in a String
def reverse(st):
    list = st.split()
    list.reverse()
    return ' '.join(list)

print (reverse("Hello world"))
