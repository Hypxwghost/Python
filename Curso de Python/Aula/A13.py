i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for x in range(i, f + 1, p):
    print(x)
print('FIM')

s = 0
for a in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
