int_list = []
float_list = []

n = int(input("Enter element count: "))

for i in range(n):
    int_list.append(int(input("Enter element: ")))

for i in range(len(int_list)):
    float_list.append(float(int_list[i]))

print(float_list)