print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('Este é um triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo isósceles!')
    else:
        print('Este é um triângulo escaleno!')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulos!')
