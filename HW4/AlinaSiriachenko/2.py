# Task2. Create a list that contains elements of integer 
# type, then use the loop to change the type of these 
# elements to a floating type. 
# (Hint: use the built-in float () function). 


list = [1, 2, 3, 4, 5]
new_list = []
for el in list:
    el = float(el)
    new_list.append(el)
print(new_list)
