from time import sleep

pmaior = 0
pmenor = 0
for x in range(1, 6):
    peso = input('Digite o peso da {}° pessoa: '.format(x))
    if x == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('Calculando...')
sleep(5)
print('O maior peso foi de {}Kg'.format(pmaior))
print('O menor peso foi de {}Kg'.format(pmenor))
