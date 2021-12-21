# # a = {45:"67", 
# #      78:"67", 
# #      89:"777"}

# # print(a)

# # PATH1 = "\path\table\name"
# # PATH2 = r"\path\table\name"

# # print(PATH1)
# # print(PATH2)

# # name = "John"
# # age = 23
# # salary = 999.99
# # # print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))

# # default_order = f"Hello, {salary}, {age} and {name}"
# # print(default_order)
# # order using positional argument
# # positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# # print(positional_order)
# # # order using keyword argument
# # keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# # print(keyword_order)


# str = 'programiz'
# print('str[:] = ', id(str), id(str[:]))


# t = "PrOgRaMiZ"
# d = t.upper()
# print(id(t), id(d))

# from re import *

# print(dir())

# def testing_def_args(name, msg = 'Text here'):
#     print('Some text', msg, name)

# testing_def_args('Test_user', msg='lalalala')

# def func_with_args(*args):
#     print(args)

# print(func_with_args(*'STRANGE WORDS'))

# import base64

# message = "Python is fun"
# message_bytes = message.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')

# print(message_bytes.decode())
# print(base64_bytes)
# print(base64_message)

# x = 'Outside of the func text'

# def sneaking_out():
#     global x 
#     x = x + "111"
#     print(x)

# sneaking_out()
# print(x)
# x =20
# def non_local_func():
#     x = 1473
#     print('non_l func', x)
#     def local_func():
#         # print('before assigment', x)
#         x = 1111
#         print('after assigment', x)
    
#         def even_further():
#             nonlocal x
#             print('frominside of inside', x)
#         even_further()
    
#     local_func()

# non_local_func()
