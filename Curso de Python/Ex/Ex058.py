from random import randint
from time import sleep

pc = 1
jogador = 0
contador = 0
pc2 = randint(0, 10)
opcao = int(input('''Digite um opção para selecionar a dificuldade:
[1] Fácil
[2] Dificil
[3] Ultimate
# todo adicionar nova dificuldade "impossivel"'''))
while True:
    try:
        contador += 1
        pc = randint(0, 10)  # gera número aleatório
        print(' ' * 20)
        print('-=-' * 20)
        print('\033[35mVou "pensar" em um número entre 0 e 10.Tente adivinhar\033[m')
        print('-=-' * 20)
        jogador = int(input('Em que número eu "pensei?"'))
        print('PROCESSANDO...')
        sleep(1)
        if jogador == pc or jogador == pc2:
            print('\033[4;34mPARABÉNS! Você conseguiu me vencer após {} tentativas!\033[m'.format(contador))
            opcao2 = input('S- Continuar \nN- Sair').upper()
            if opcao2 == 'N':
                break
        elif jogador < pc and opcao == 3:
            print('\033[32mMais... Tente mais uma vez.\033[m')
        elif jogador > pc and opcao == 3:
            print('\033[34mMenos... Tente mais uma vez.\033[m')
        elif jogador < pc2 and opcao == 1:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc2 and opcao == 1:
            print('Menos... Tente mais uma vez.')
        else:
            print('\033[36mGANHEI!,mais sorte na próxima !\033[m')
    except ValueError:
        print('\033[7;40;31mDigite apenas números!\033[m')
