dano = 2143

conv_to_str = str(dano)

multiplication = int(conv_to_str[-1]) * int(conv_to_str[2]) * int(conv_to_str[1]) + int(conv_to_str[0])

print(multiplication)

reversed_dano = conv_to_str[-1] + conv_to_str[2] + conv_to_str[1] + conv_to_str[0]

print(int(reversed_dano))

sorted_dano = sorted(reversed_dano)

sorted_dano_united = str

sorted_dano_united = sorted_dano[0] + sorted_dano[1] + sorted_dano[2] + sorted_dano[3] 

print(int(sorted_dano_united))
