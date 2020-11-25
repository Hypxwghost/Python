print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
a = 0
while cont <= a:
    print('{} -> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('FIM')
