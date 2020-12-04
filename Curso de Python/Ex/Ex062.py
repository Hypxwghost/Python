print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quanto termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
