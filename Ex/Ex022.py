n = input('Digite seu nome completo').strip()
print('Analisando seu nome...')
print('Seu nome em masiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
print('Seu nome possuí {} letras'.format(len(n)-n.count(' ')))
# print('Seu primeiro nome possuí {} letras'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
