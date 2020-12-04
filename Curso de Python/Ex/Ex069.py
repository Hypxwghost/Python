tot18 = toth = totm20 = 0
while True:
    try:
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade < 20:
            totm20 += 1
        resp = ' '
        while resp not in 'SN':
            resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp == 'N':
            break
    except ValueError:
        print('Digite apenas números !')
print(
    f'Dente todas as pessoa,tivemos {tot18} pessoas com mais de 18 anos,{toth} homens e {totm20} mulheres com menos de 20 anos!')
