#task 2 (знайти добуток числа)
print("Task 2")
num = 4586
num2 = 1
while (num != 0):
    num2 = num2 * (num % 10)
    num = num // 10
print("Добуток: ", num2)

#task 2.1 (записати число у реверсному порядку)
print("Task3")
num = str(4586)
num = num[:: -1]

print("reversne chyslo: " + num)
