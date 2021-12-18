# Input number and calculate factoryal of this number

number_from_user = int(float(input('Please input number factorial of which you are looking for: ')))

if number_from_user < 0: 
    print("Factoriql of negative number doesn't exist, script would be terminated now" )
elif number_from_user <= 1:
    print("Factorial's value is equal 1")
elif number_from_user > 1:
    factorial_value=number_from_user
    for verable_for_factorial_calculation in range(1,number_from_user):
        factorial_value*=verable_for_factorial_calculation
    print(f"Factoral's value is equal {factorial_value}")
