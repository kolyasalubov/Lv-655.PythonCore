def word():
    d={}
    for key in a:
        value=a.count(key)
        d.update({key:value})
    return(d)

a=input('Input word: ')
print(word())



# # def word(**kwargs):
# #     kwargs=list(a)
# #     d={}
# #     for kwarg1 in kwargs:
# #         kwarg2=kwargs.count(kwarg1)
# #         d.update({kwarg1:kwarg2})
# #     return kwargs 

# # print(word())    


# 
 

# def word():
#     for litera in a:
#     amount=a.count(litera)
#     print({litera:amount})

# print(word()) 