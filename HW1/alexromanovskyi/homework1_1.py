# Output question “What is your name?“, 
#                                    “How old are you?“, 
#                                    “Where do you live?“. 
# Read the answer of user and output next information: “Hello, (answer(name))“, 
# “Your age is  (answer(age))“, 
# “You live in  (answer(city))“.   
 

user_name = input("What is your name?:")
print ("Hello,",(user_name))

user_age = int(input("How old are you?:"))
print ("Your age is",(user_age))

user_city = input ("Where do you live?:")
print ("You live in", (user_city))