number = 3756
product = 1

while number != 0:
    product *= number % 10
    number //= 10

print("Product:", product)

# ----------

number = 3756
print("Reverse number:", str(number)[::-1])

# ----------

number = 3756
print("Sorted digits:", sorted(str(number)))

# ----------

a = 12
b = 24

a, b = b, a

print(a, b)