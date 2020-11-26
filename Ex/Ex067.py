while True:
    try:
        num = int(input('Digite um número para calcular sua tabuada: '))
        if num < 0:
            print('Número negativos não são aceitos!')
            break
        cont = 0
        while cont < 10:
            cont += 1
            resp = num * cont
            print(f'{cont} X {num} = {resp}')
        opcao = input('''
        C - Continuar
        S - Sair''').upper()
        if opcao == 'S':
            break
    except ValueError:
        print('Digite um número válido: ')
