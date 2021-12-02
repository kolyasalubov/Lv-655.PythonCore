# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.


#1 arephmetic method fot int , return float
a=-4
b=5
print("#1 "+"_"*20 +"\n",f"BEFORE a = {a} b = {b}")

a = a * b 
b = a / b 
a = a / b  
print(f" AFTER a = {a} b = {b}")

a=3
b=10

print("#2 "+"_"*20 +"\n",f"BEFORE a = {a} b = {b}")

#2 arephmetic method for int 
a = a + b 
b = a - b 
a = a - b 
print(f" AFTER a = {a} b = {b}")


#3 unpacking tuple method
a1="boba"
b1=77
print("#3 "+"_"*20 +"\n",f"BEFORE a = {a1} b = {b1}")
(a1,b1) = b1,a1 

print(f" AFTER a = {a1} b = {b1}")
