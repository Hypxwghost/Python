print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('FIM')
