a,b = 1,1


try:
    a = int(input('Please input integer value for a: '))
except:
    try:
        a = int(input("Only integare values are allowed, let's try againe, please input int value for a: "))
    except:
        print('Since non int value was entered for a, script would be terminated')
        exit()

try:
    b = int(input('Please input integer value for b '))
except:
    try:
        a = int(input("Only integare values are allowed, let's try againe, please input int value for b: "))
    except:
        print('Since non int value was entered for b, script would be terminated')
        exit()

print('Result for operation a + b is:' ,a + b)
print('Result for operation a - b is:' ,a - b)
print('Result for operation a * b is:' ,a * b)
print('Result for operation a / b is:' ,a / b)
print('Result for operation a ** b is:' ,a ** b)