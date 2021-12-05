# Task 1 Simple: Find The Distance Between Two Points

def coordinates(p1, p2):
    i = 0
    result = 0
    d = 0
    if len(p1) == len(p2) and len(p1) != 0:
        while i < len(p1):
            d = d + (p1[i] - p2[i])**2
            i += 1
    else:
        return -1
    result = d**0.5
    return result

# Task 2 No Yelling!

def filter_words(st):
    st = st.capitalize()
    return st

# 3 Task Unfinished loop - Bug fixing #1

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

# Task 4 Convert a Number to a String!

def number_to_string(num):
    num = str(num)
    return num

# Task 5 Reversing Words in a String

def reverse(st):
    if st == "":
        return st
    st_s = st.split(" ")
    for i in st_s:
        if i == "":
            return st
    st_r = st_s[::-1]
    st_j = " ".join(st_r)
    return st_j

# Task 6 Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
