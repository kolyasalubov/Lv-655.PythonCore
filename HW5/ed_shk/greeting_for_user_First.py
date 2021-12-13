#greet user if his login is first

USER_LOGIN = "First"

while True:
    x = input("Enter your login: ")
    if x == USER_LOGIN:
       print("Hello, ", x)
       break
    elif x == "help":
       print("Take your card and farewell!")
       break
    else:   
       print("Error ocurred")
       print("If you want to leave enter 'help'")
     
    
