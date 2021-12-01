

while True:
    number_ = input("Please input number from 1000 to 9999: ")
    if number_.isdecimal() and number_.isdigit() and len(number_)<5 and len(number_)>3:
        break

product = 1
reversed_number=''
for x in number_:
    product *=int(x)
    reversed_number=x+reversed_number

number_list = list(number_)
number_list.sort()

print ("Product of multiplication: " + str(product))
print ("Reversed number: " + reversed_number)
print ("Sorted number: " + str(number_list))


