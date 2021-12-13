# katas for homework 6
"""
Given two ordered pairs calculate the distance between them. Round to two decimal places. 
This should be easy to do in 0(1) timing.
"""
def distance(x1, y1, x2, y2):
    import math
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

"""
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny,
and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
"""
def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)

"""
Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
String should be capitalized and properly spaced. Using re and string is not allowed.
"""
def filter_words(st):
    ns = st.capitalize()
    result = " ".join(ns.split())
    return result


"""
You need to write a function that reverses the words in a given string. A word can also fit an empty string.
If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
"""
def reverse(st):
    st_reverse = []
    words = st.split()
    for word in range(len(words) - 1, -1, -1):
        st_reverse.append(words[word])
    return " ".join(st_reverse)

"""
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
"""
def create_array(n):
    res=[]
    for item in range(n):
        res.append(item + 1)
    return res 

"""We need a function that can transform a number into a string.
What ways of achieving this do you know?
"""
def number_to_string(num):
    return str(num)
