#Write a script that will calculate the factorial of the entered number  without using recursion.
#import math
#print (math.factorial(5)) 

input_fact= int(input("Input count fact: "))
fact = 1
for i in range(1,input_fact+1): 
    fact*=i    
   
print (f"fact = {fact}") if input_fact>0 else  print("fact = 1")

