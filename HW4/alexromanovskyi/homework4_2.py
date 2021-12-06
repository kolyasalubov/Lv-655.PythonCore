#Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
#(Hint: use the built-in float () function). 

a = int(input("Number_1: "))
b = int(input("Number_2: "))
c = int(input("Number_3: "))
d = int(input("Number_4: "))

list = [a,b,c,d]
float_list = []
for fl in list:
    fl = float(fl)
    float_list.append(fl)
print (float_list)