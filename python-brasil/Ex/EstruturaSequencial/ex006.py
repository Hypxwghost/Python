try:
    r = int(input('Digite a o raio do circulo: '))
    a = 3.14 * r**2

    print(f'A área do circulo é: {a}')
except ValueError:
    print('Número não é um inteiro ou é inválido')