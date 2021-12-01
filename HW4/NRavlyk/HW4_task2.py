number = 0
while True:
    number_str = input("Please input number : ")
    try:
        number = int (number_str)
        if number > 0:
            break           
    except:
        print("Once more")

listofnumber = list(range(0,number,2))

print(listofnumber)

for x in range(0,len(listofnumber)):
    listofnumber[x] = float(listofnumber[x])
print(listofnumber)
