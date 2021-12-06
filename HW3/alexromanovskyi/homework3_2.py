#A four-digit natural number is specified.
# Find the product of the digits of this number.
value = input("enter a four-digit number: ")
dobut = int(value[0])+ int(value[1])+int(value[2])+int(value[3])

print("Dobutok= ", dobut)

#Write the number in reverse order.
revers = int(str(value)[::-1])

print("Revers: ", revers)

#Sort the numbers included in this number
sort = int(value)
sort = sorted(str(value))

print("Sort: ", sort)