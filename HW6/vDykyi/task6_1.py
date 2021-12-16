def comprasion(change1, change2):
    """This function compares two diffrent values and return larger """
    if change1 > change2:
        return change1
    else:
        return change2    

value1 = float(input("Pleas write some number: "))
value2 = float(input("Pleace write some number: "))

print(comprasion(value1, value2)) 
