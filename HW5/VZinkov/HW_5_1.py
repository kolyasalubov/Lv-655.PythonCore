even2=[]
odd3=[]
not2or3=[]
for i in range (1,11):
    if i%2==0:
        even2.append(i)
    elif i%3==0:
        odd3.append(i)
    elif i%2!=0 and i%3!=0:
        not2or3.append(i)
print(even2)
print(odd3)
print(not2or3)

