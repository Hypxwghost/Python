print('Calculadora de números pares!')
n = int(input('Fim: '))
opcao = int(input('''
[ 1 ] Par
[ 2 ] Ímpar'''))
if opcao == 1:
    o = 'pares'
else:
    o = 'ímpares'
print('Os números {} até {} são: '.format(o, n))
if opcao == 1:
    for x in range(2, n+1, 2):
        print(x, end=' ')
elif opcao == 2:
    for x in range(1, n+1, 2):
        print(x, end=' ')
else:
    print('\033[4;31mDADOS INVÁLIDOS!!')
