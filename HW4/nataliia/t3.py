n = int(input("Enter number: "))
if n<0:
    print("Negative number not allowed")
else:
    n_0 = 0
    n_1 = 1
    n_2 = 1
    step = 0
    while step < n:
        print(n_0)
        n_0 = n_1
        n_1 = n_2
        n_2 = n_1 + n_0
        step = step + 1