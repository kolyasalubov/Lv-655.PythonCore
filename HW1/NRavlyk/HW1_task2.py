# Порядок виконання 
# (expressions...), [expressions...], {key: value...}, {expressions...}
#     'Binding or parenthesized expression, list display, dictionary display, set display'

# x[index], x[index:index], x(arguments...), x.attribute
#     'Subscription, slicing, call, attribute reference'

# await x
#     'Await expression' 

# **  Exponentiation
# +x, -x, ~x  Positive, negative, bitwise NOT
# *, @, /, //, %  Multiplication, matrix multiplication, division, floor division, remainder 6
# +, -  - Addition and subtraction
# <<, >> Shifts
# & Bitwise AND
# ^ Bitwise XOR
# | Bitwise OR
# in, not in, is, is not, <, <=, >, >=, !=, ==  Comparisons, including membership tests and identity tests
# not x Boolean NOT
# and Boolean AND
# or Boolean OR
# if – else Conditional expression
# lambda Lambda expression
# := Assignment expression

x = float(input("Please input x:"))
y = float(input("Please input y:"))

print ('x + y =', x + y)
print ('x - y =', x - y)
print ('x * y =', x * y)
print ('x / y =', x / y)
print ('x % y =', x % y)
print ('x // y =', x // y)
print ('x ** y =', x ** y)

number = 3 + 4 * 5 ** 2 + 7
print('3 + 4 * 5 ** 2 + 7 =', number)
number = (3 + 4) * (5 ** 2 + 7)
print('(3 + 4) * (5 ** 2 + 7) =',number)
number = 2**3**2
print('2**3**2 =', number)
number = (2**3)**2
print('(2**3)**2', number)