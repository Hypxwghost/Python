num = int(input('Digite um número: '))

num_list = []

for n in range(1, num+1):
    num_list.append(n)
    print('{:>4}'.format(n), end='')
    if n % 6 == 0:
        print()

