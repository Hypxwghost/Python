frase = 'pão de queijo lorem ipsum'.lower().replace(' ','')

num = 0

letra_list = []
letra_repetida = []

for letra in frase:
    if letra in letra_list:
        if letra in letra_repetida:
            pass
        else:
            print(letra, num)
            letra_repetida.append(letra)
    else:
        print(letra, ':', 1)
        letra_list.append(letra)
