# ----------2.Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

number = 1234
number_str = str(number)
numbers_list = list(number_str)

number_multiplied = number * number
number_reversed = int(number_str[::-1])
number_sorted = sorted(numbers_list)
print(f'Multiply = {number_multiplied}, reversed = {number_reversed}, sorted = {number_sorted}')