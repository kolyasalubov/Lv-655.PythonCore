my_list=[1, 2, 3, 4, 5, 6, 7]
for num in my_list:
    print(float(num))
    
  

#########################################################


int_list=[int(i) for i in input('Input integer numbers: ').split()]
float_list=[]
for i in int_list:
        float_list.append(float(i))

print(float_list)    