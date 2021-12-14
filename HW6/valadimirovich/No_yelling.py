def filter_words(st):
    # Your code here.
    st = st.lower()
    st = st.capitalize()
    st = ' '.join(st.split())
    print(st)
    return st
