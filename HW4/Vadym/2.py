# Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
# (Hint: use the built-in float () function). 


our_list= [3,6,4,3,32,666,6]
print(our_list)

#1 Whitout loops
our_list = list (map(float,our_list))
print(our_list)

#2 Use enumerate
for index, item in enumerate(our_list):
     our_list[index] = float(item)
print(our_list)

#3 Same..
for index in range(len(our_list)):
    our_list[index] =float (our_list[index])
print(our_list)