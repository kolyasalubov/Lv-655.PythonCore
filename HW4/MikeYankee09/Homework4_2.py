list1 = []
x = int(input("Please enter the number of digits in sequirence :"))
for item in range(x):
    list1.append(int(input("Please enter a digit")))
list2 = []
for item in list1:
    item = float(item)
    list2.append(item)
print(list2)
