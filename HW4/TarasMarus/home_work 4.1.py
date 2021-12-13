n=int(input("введіть число "))
f=1

while n > 1:
  f = n * f
  n = n - 1
      
print("факторіал числа =",f)