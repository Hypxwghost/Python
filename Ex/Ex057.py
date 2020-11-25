sexo = input('Informe seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'MmFf':
    try:
        sexo = input('Dados inválidos!.Digite seu sexo corretamente: ').upper().strip()[0]
    except ValueError:
        print('Digite uma idade válida!')
print('Seco {} regstrado com sucesso'.format(sexo))
