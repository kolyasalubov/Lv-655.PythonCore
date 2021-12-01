number = 0
while True:
    number_str = input("Please input number : ")
    try:
        number = int (number_str)
        break         
    except:
        print("Once more")


number_factorial = 1
for x in range(1,number+1):
    number_factorial *= x

print (f"factorial of the {number} will be: " + str(number_factorial))
