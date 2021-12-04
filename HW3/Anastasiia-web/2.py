# 1. Знайти добуток цифр цього числа
digit_1 = int(n/1000)
digit_2 = int(n/100)%10
digit_3 = int(n/10)%(int(n/100))
digit_4 = n%(int(n/10))                                                

digits_multiplication = int(n/1000) * (int(n/100)%10) * (int(n/10)%(int(n/100))) * (n%(int(n/10)))

print(digits_multiplication)
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
