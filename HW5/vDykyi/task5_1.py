# Task5_1
     
num_list1 = []
num_list2 = []
num_list3 = []

for i in range(1, 11):
      if i % 2 == 0:
           num_list1.append(i)
      elif i % 3 == 0:
            num_list2.append(i) 
      elif i % 2 != 0 and i % 3 != 0:
           num_list3.append(i)
          
print("Numbers divisible by 2: ", num_list1)
print("Numbers divisible by3: ", num_list2)
print("Numbres that are not divisible 2 and 3: ", num_list3)

