from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pes)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoa maiores de idade'.format(totmaior))
print('E também tivemos {} pessoa menores de idade'.format(totmenor))
