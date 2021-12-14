# Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

size = int(input("Enter the number  Fibonacci \n"))
first = 1
second = 1
for range in range(size):  
    print(first,end = ",")
    sum = first + second
    first = second
    second = sum
    
  