# make calculation with given number
def calculation(x):

    digits = []

    # calculate product and fill list for sorting
    product_4digits = 1
    for dig in x:
        digits.append(int(dig))
        product_4digits = product_4digits * int(dig)

    # reverse digits
    reverse_number = x[3::-1]

    # sort and fix in string
    sorted_number = ''
    digits_sorted = sorted(digits)
    for dig in digits_sorted:
        sorted_number = sorted_number + str(dig)

    # print results
    print("\nNumber:", x)
    print("Product of digits: ", product_4digits)
    print("Digits in reverse order: ", reverse_number)
    print("Sorted digits: ", sorted_number)

    return True

# ask user for number
while True:
    print("Here we do some operations with interger 4-digit numbers")
    number_for_analysis = input("Please, eneter some 4-digit number ")
    try:
        if int(number_for_analysis) >= 1000 and int(number_for_analysis) <= 9999:
            calculation(number_for_analysis)
            break
        else:
            print("Number must be in 1000 and 9999 range\n")
    except ValueError:
        print("This is not interger 4-digit number. Try again\n")
