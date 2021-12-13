# Написати скрипт- calculator.py, в якому створюєте функції додавання, віднімання, множення, ділення, 
# а в іншому модулі запитуєте користувача, яку дію він хоче виконати і з якими числами.

def addition(summand_one:float, summand_two:float)->float:
    return summand_one+summand_two

def subtraction(minuend:float, subtrahend:float)->float:
    return minuend-subtrahend

def multiplication(multiplicanda_one:float, multiplicanda_two:float)->float:
    return multiplicanda_one*multiplicanda_two

def division(dividend:float, divisor:float)->float:
    return dividend/divisor
