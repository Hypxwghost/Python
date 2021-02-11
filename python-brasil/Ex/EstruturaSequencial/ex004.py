num_list = []
soma = 0

for x in range(1, 5):
    num = int(input(f'Digite o {x}°Número: '))
    soma += num
print(f'A média é: ', soma/4)
