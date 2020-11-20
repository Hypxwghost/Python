import datetime

ano = input('Digite o ano de nascimento do atleta: ')
dataa = datetime.date.today()
anoa = dataa.year
idade = int(ano) - int(anoa)
idade = idade - (idade * 2)
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Este é um atleta MIRIM!')
elif idade <= 14:
    print('Este é um atleta INFANTIL!')
elif idade <= 19:
    print('Este é um atleta JUNIOR!')
elif idade <= 25:
    print('Este é um atleta SÊNIOR!')
else:
    print('Este é um atleta MASTER!')
