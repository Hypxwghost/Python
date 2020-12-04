cont = num = s = 0
while True:
    try:
        num = int(input('Digite um número[999 para parar]: '))
        if num == 999:
            break
        cont += 1
        s += num
    except ValueError:
        print('Digite um número válido!!')
print(f'A soma entre os {cont} valores é {s}')
