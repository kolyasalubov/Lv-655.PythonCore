def reverse(st):
    l1=st.split()
    l1.reverse()
    return ' '.join(l1)


print(reverse('How are   you doing?'))