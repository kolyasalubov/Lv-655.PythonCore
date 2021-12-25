text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better, than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one - -obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - - let's do more of those!"""

# # Task 1 (amount of better, never, is )
amount_better = text.count("better")
amount_never = text.count("never")
amount_is = text.count("is")
print("Amount of better:", amount_better, "amount of never:",
      amount_never, "amount of is:", amount_is)

# (upper)
text_upper = text.upper()
print(text_upper)

# (replace)
text_replaced = text.replace("i", "&")
print(text_replaced)

# Task 2 Добуток

number = 5932
mul = 1
sum = 0

n = str(number)
n0 = int(n[0])
n1 = int(n[1])
n2 = int(n[2])
n3 = int(n[3])
number_m = n0*n1*n2*n3
print(number_m)

while number > 0:
    digit = number % 10
    mul *= digit
    sum += digit
    number //= 10

print(mul)
print(sum)

# reverse a number
# first option

n4 = str(number)[::-1]
n5 = int(n4)
print(n5)

n_1 = 6834
n_2 = 0

# second option 
while n_1 > 0:
    digit = n_1 % 10
    n_1 //= 10
    n_2 *= 10
    n_2 += digit

print(n_2)

# sort
n6 = str(number)
n7 = list(n6)
n7.sort()
print(n7)

# Task 3 change
a = 5567
b = 23
a, b = b, a
print(a, b)


n1 = 9430
n2 = 0
n3 = 1

while n1 > 0:
    d = n1 % 10
    n2 += d
    n3 *= d
    n1 = n1 // 10

print(n2, n3)
