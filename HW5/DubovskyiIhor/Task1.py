my_list=[1,2,3,4,5,6,7,8,9,10]
even=[num for num in my_list if num%2==0]
odd=[num for num in my_list if num%2==1 and num%3==0]
others=[]
for num in my_list:
    if num not in even and num not in odd:
        others.append(num)
       

print('Even numbers: ', even)
print('Odd numbers, which are divisible by 3: ', odd)
print('Numbers that are not divisible by 2 and 3: ', others)