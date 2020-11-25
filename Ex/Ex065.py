while True:
    try:
        num = int(input('Digite um número: '))
        media = num + num
        media = media / media
        opcao = str(input('Quer continuar? [S/N]: ')).upper()
        if opcao == 'N':
            break
    except ValueError:
        print('Valores digitados inválidos!')
print('A média entre os valores é {}'.format(media))
