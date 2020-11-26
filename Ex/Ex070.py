total = totmil = menor = cont = 0
barato = ' '
while True:
    try:
        produto = input('Nome do produto: ')
        preco = float(input('Preço: R$'))
        cont += 1
        total += preco
        if preco > 1000:
            totmil += 1
        if cont == 1 or preco < menor:
            menor = preco
            barato = produto
        resp = ' '
        while resp not in 'SN':
            resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp == 'N':
            break
    except ValueError:
        print('Digite apenas números!')
print('{:-^40}'.format('FIM'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
