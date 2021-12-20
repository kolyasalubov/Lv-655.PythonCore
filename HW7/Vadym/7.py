
# Counting sheep...
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(sheep):
   return len(list(x for x in sheep if x))

    #2 return sheep.count(1)

print(count_sheeps(array1))
  
  