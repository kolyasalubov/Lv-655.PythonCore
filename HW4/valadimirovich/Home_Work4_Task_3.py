
entered_n=int(float(input('Please enter index of the Fibbonacci sequence: ')))

counter=0

fibonacci_n_1=0

fibonacci_n_2=1

print(f"Here is you fibonacci sequence [ {fibonacci_n_1} {fibonacci_n_2}", end=" ")

while counter<entered_n-1:
    Fibonacci_current=fibonacci_n_1+fibonacci_n_2
    fibonacci_n_1=fibonacci_n_2
    fibonacci_n_2=Fibonacci_current
    counter+=1

    print(f"{Fibonacci_current}", end=" ")

print("]\nTa-da! which is short for 'ta-tarada-dam' why would you ask ? because optimization is important!")
