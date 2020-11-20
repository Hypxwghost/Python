n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
