somaidade = 0
mediaidade = 0
midh = 0
nomev = ''
totm20 = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        midh = idade
        nomev = nome
    if sexo in 'Mm' and idade > midh:
        midh = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {}anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(midh, nomev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm20))
