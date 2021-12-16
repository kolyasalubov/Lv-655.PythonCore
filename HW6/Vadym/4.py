# We need a function that can transform a number into a string.
# What ways of achieving this do you know?
#123 --> "123"

a = 123
print (type(a))
#1
print (type(str(a)))
#2
print(type(f"{a}"))
#3
print (type("% s" % a))

