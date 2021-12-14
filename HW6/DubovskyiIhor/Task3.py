def word():
    d={}
    for key in a:
        value=a.count(key)
        d.update({key:value})
    return(d)

a=input('Input word: ')
print(word())



 