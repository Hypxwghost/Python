res = 0
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        opcao = int(input('''O que você deseja fazer com esses números?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair'''))
        if opcao == 1:
            res = num1 + num2
            print('A soma entre {} e {} é {}'.format(num1, num2, res))
        elif opcao == 2:
            res = num1 * num2
            print('A multiplicação entre {} e {} é {}'.format(num1, num2, res))
        elif opcao == 3:
            if num1 > num2:
                print('O número {} é maior'.format(num1))
            elif num2 > num1:
                print('O número {} é maior'.format(num2))
            else:
                print('Os dois números são iguais!')
        elif opcao == 5:
            break
        else:
            print('Digite uma opção válida!')
    except ValueError:
        print('Digite valores válidos!')
