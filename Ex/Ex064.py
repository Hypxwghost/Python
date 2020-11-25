contador = 0
p = 0
soma = 0
while p != 999:
    try:
        p = int(input('Digite um número'))
        soma = p + p
        contador += 1
        if p == 999:
            contador = contador - 1
            break
    except ValueError:
        print('Digite um número válido !')
print('No total foram digitados {} números e a soma entre eles é {}'.format(contador, soma))
