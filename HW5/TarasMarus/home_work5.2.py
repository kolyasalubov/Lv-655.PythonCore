# L1=[]
# L2=[]
# L3=[]
# x=0
# while x in range(10):
#     if x % 2==0:
#         L1.append(x)
#     x+=1
#     if x % 3 == 0:
#         L2.append(x)
#     if x % 2!=0 and x % 3!=0:
#         L3.append(x)
# print("numbers divisible by 2:",L1, "\nnumbers divisible by 3:",L2 ,"\nnumbers that are not divisible by 2 and 3:",L3)
    
    
lut1 =[x for x in range(1,10) if x%2==0]
lut2 =[x for x in range(1,10) if x%3==0]
lut3 =[x for x in range(1,10) if x%2!=0 and x%3!=0]
print("numbers divisible by 2:",lut1, "\nnumbers divisible by 3:",lut2 ,"\nnumbers that are not divisible by 2 and 3:",lut3)

