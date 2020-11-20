n1 = input('Digite o primeiro valor: ')
n2 = input('Digite o segundo valor: ')

if n1 > n2:
    print('O número \033[4;31m{}\033[m é \033[4;35mmaior\033[m'.format(n1))
elif n1 < n2:
    print('O número \033[4;31m{}\033[m é \033[4;35mmaior\033[m'.format(n2))
else:
    print('\033[4:31mNão existe valor maior.OS dois são iguais')
