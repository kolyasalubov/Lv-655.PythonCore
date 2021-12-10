import calculator

number_one=float(input("please enter number one: "))
number_two=float(input("please enter number two: "))

math_operand = input("please inpute typy of mathematical operations - +-*/ : ")

result=0
if math_operand=='+':
    result=calculator.addition(number_one,number_two)
elif math_operand=='-':
    result=calculator.subtraction(number_one,number_two)
elif math_operand=='*':
    result=calculator.multiplication(number_one,number_two) 
elif math_operand=='/':
    result=calculator.division(number_one,number_two) 
else:
    print("something wrong")
    quit

print(f"{number_one} {math_operand} {number_two} = ",result) 
