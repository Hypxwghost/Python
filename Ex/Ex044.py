print('{:=^40}'.format('LOJA DO JUNIN'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalp = int(input('Quantas parcelas? '))
    parcela = total / totalp
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(totalp, parcela))
else:
    print('\033[4;31mDADOS INVÁLIDOS,TENTE NOVAMENTE !!\033[m')
    total = 0
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
