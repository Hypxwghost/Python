from random import randint, choice

numf = escolha = 0

while True:
    try:
        print('-' * 40)
        escolha = int(input('''
        [1] - Sorteador de números
        [2] - Sorteador de 'True' 'False'
        '''))
        if escolha == 1:
            print('-' * 40)
            numf = int(input('Digite o número final(O primeiro é 1): '))
            print('-' * 40)
            num = randint(1, numf)
            print('O número sorteado :', num)
            print('-' * 40)
            continua = input('Continuar? [S/N]: ').upper()
            print('-' * 40)
            if continua == 'N':
                break
        elif escolha == 2:
            escolha = choice([True, False])
            if escolha == True:
                print('"Sim/Verdade" foi sorteado')
            else:
                print('"Não/Falso" foi sorteado')
    except ValueError:
        print('Digite apenas números !')
