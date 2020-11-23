print('\033[31mCalculadora de tabuadas V2!\033[m')
n = int(input('Digite um número inteiro: '))
for x in range(0, 11):
    print(('\033[36m{}\033[m x \033[35m{}\033[m = \033[31m{}\033[m'.format(n, x, n*x)))
