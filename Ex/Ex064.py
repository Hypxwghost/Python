contador = num = soma = 0
try:
    num = int(input('Digite um número [999 para parar]'))
except ValueError:
    print('Digite um valor válido')
while num != 999:
    try:
        soma += num
        contador += 1
        num = int(input('Digite um número [999 para parar]'))
    except ValueError:
        print('Digite um número válido !')
print('No total foram digitados {} números e a soma entre eles é {}'.format(contador, soma))
