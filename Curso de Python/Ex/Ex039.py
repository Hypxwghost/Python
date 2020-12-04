import datetime
ano = int(input('\033[32mDigite seu ano de nascimento: \033[m'))
dataa = datetime.date.today()
anoa = dataa.year
idade = ano - int(anoa)
idade = idade - (idade * 2)
print('\033[34mQuem nasceu em\033[m \033[1;4;35m{}\033[m \033[34mtem\033[m \033[1;4;35m{}\033[m \033[34manos\033[m '
      '\033[34mem\033[m \033[1;4;35m{}\033[m'.format(ano, idade, anoa))
if idade < 18:
    saldo = 18 - idade
    print('\033[1;34mVocê ainda não pode se alistar,faltam \033[4:31m{}\033[m \033[34manos.\033[m'.format(saldo))
    ano = anoa + saldo
    print('\033[34mSeu alistamento será em\033[m \033[4;31m{}\033[m'.format(ano))
elif idade == 18:
    print('\033[4;31mJá é hora de sofrer!\033[m \033[4:31mkkkkkkkkkkkkkkkkk\033[m \n \033[1;31mPress F\033[m')
else:
    saldo = idade - 18
    print('\033[4;31mVocê está {} anos atrasado,vai lá correndo!\033[m'.format(saldo))
    ano = anoa - saldo
    print('Seu alistamento foi em \033[4;31m{}'.format(ano))
