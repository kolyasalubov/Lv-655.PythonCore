#Задано чотирицифрове натуральне число.
#- Знайти добуток цифр цього числа.
#- Записати число в реверсному порядку.
#- Посортувати цифри, що входять в дане число

a = input('Input number : ')

# parcing number to list
a = list (map(int, a))
print(a)


# Use bild in func and concatenate list
print("Sorted :", int(''.join(map(str,sorted(a)))))  
print("Sum :", int(''.join(map(str,str(sum(a))))))  #sum back int ! -> str for .join
print("Reversed :", int(''.join(map(str,a[::-1])))) # reverse by List Slicing
print("Reversed #2 :", int(''.join(map(str,list(reversed(a)))))) # reverse by function reversed()