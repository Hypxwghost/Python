num = 1
par = impar = 0
while num != 0:
    try:
        num = int(input('Digite um valor inteiro: '))
        if num != 0:
            if num % 2 == 0:
                par += 1
            else:
                impar += 1
    except ValueError:
        print('Entrada invalida!')
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
