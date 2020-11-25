print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while mais != 0:
    while cont <= 10:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
mais = int(input('Quanto termos você quer mostrar a mais? '))
