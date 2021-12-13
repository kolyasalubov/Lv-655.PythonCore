# Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. 

# Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
from random import randint

number = randint(1,100)
print(number)

copmlite_the_game = False
while not copmlite_the_game:
    n = int(input("please input number between 1..100: "))
    if n==number: 
        copmlite_the_game = True
    elif n>number:
        print("Your number is bigger")
    elif n<number:
        print("Your number is smaller") 

print("You win: number is ", n)
