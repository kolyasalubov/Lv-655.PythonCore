number = 0
while True:
    number_str = input("Please input number : ")
    try:
        number = int (number_str)
        break         
    except:
        print("Once more")

listofnumber = list(range(number))

print(listofnumber)

for x in listofnumber:
    listofnumber[x] = float(listofnumber[x])
print(listofnumber)
