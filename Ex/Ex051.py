a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
de = a1 + (10 -1) * r
for x in range(a1, de+r, r):
    print('{} '.format(x), end=' -> ')
print('ACABOU!')