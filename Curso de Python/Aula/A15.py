n = s = 0
while True:
    try:
        n = int(input('Digite um número: '))
        if n == 999:
            break
        s += n
    except ValueError:
        print('Digite um número válido !')
print(f'A soma vale {s}')
