massa = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))
imc = massa / (altura * altura)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Esta pessoa está abaixo do peso !!')
elif 18.5 < imc < 25:
    print('Esta pessoa está no peso ideal !')
elif 25 < imc < 30:
    print('Esta pessoa está com Sobrepeso !')
elif 30 < imc < 40:
    print('Esta pessoa está obesa !!')
else:
    print('Esta pessoa está com obseidade mórbida !!!!')
