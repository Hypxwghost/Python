from random import randint

cont = 0
while True:
    try:
        opcao = input('\033[31m[P] - PAR  \033[36m[I] - ÍMPAR\033[m').upper()
        pc = randint(0, 999)
        num = int(input('Digite um número: '))
        res = (num + pc) % 2
        cont += 1
        p = j = t = ''
        if opcao not in 'IPip':
            print('Digite uma opção válida!')
            break
        if (pc % 2) == 0:
            p = 'Par'
        else:
            p = 'Ímpar'
        if (num % 2) == 0:
            j = 'Par'
        else:
            j = 'Ímpar'
        if res == 0:
            t = 'Par'
        else:
            t = 'Ímpar'
        print(
            f'O pc escolheu \033[34m{pc} \033[31m[{p}]\033[m,usuario escolheu \033[35m{num} \033[32m[{j}]\033[m e o total foi \033[36m{pc + num} \033[34m[{t}]\033[m.')
        if opcao == 'P':
            if res == 1:
                print('\033[4;31mVocê perdeu!,mais sorte na próxima!/\33[m')
                break
            if res == 0:
                print(f'\033[4;34mParabéns,Você Ganhou {cont} vezes seguidas !!\033[m')
        elif opcao == 'I':
            if res == 1:
                print(f'\033[4;34mParabéns,Você Ganhou {cont} vezes seguidas !\033[m')
            else:
                print('\033[4;31mVocê perdeu!,mais sorte na próxima!!\033[m')
                break
    except ValueError:
        print('Digite um número válido!')
