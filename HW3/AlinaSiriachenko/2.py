# ----------2.Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

number = 1254
number_str = str(number)
number_list = list(number_str)

multiply_count = 1
for el in number_str:
    multiply_count*= int(el)

number_reversed = int(number_str[::-1])
number_sorted = ''.join(sorted(number_list))
print(f'Multiply = {multiply_count}, reversed = {number_reversed}, sorted = {number_sorted}')
