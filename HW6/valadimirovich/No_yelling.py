def filter_words(st):
    # Your code here.
    st = st.lower()
    st = st[0].upper() + st[1:].lower()
    st = ' '.join(st.split())
    print(st)
    return st
    