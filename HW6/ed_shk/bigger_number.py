def bigger_number(first_number, second_number):
    """
        input: two numbers
        outbut: one number
        Compare two numbers
    """
    return first_number if first_number > second_number else second_number

print("Please enter two numbers")
first_number = float(input("First number: "))
second_number = float(input("Second number: "))
if first_number == second_number:
    print("Numbers are equal")
else:
    print("Bigger number: ", bigger_number(first_number, second_number))
