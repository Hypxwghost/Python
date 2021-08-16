cont = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte']
while True:
    try:
        num = int(input('Digite um número entre 0 e 20: [S - Sair]'))
        if num >= 0 and num <= 20:
            print(f'Você digitou o número {cont[num]}')
            opcao = input('Continuar ? [S/N]').upper().strip()[0]
            if opcao == 'N':
                break
        else:
            print('O número digitado não está entre 0 e 20!')
    except ValueError:
        print('Digite um número válido!')
        break
