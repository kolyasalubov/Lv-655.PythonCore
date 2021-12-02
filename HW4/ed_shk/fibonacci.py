# calculate fibonacci numbers less then given number
while True:
    try:
        # collect user's data
        number = float(input("Please enter some positive number: "))
        # check if input meet math conditions
        if number >= 0:
            first_num = 0 
            second_num = 1
            # calculate and print fibonacci numbers
            print("\nFibbonacci numbers equal or less than ", number)            
            print(first_num)
            while second_num <= number:
                print(second_num)
                first_num, second_num = second_num, first_num + second_num
            break
        else:
            print("Only positive numbers accepted. Try again")
    except ValueError:
        print("Only numbers accepted. Try again")
        