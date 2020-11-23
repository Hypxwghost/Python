num = int(input('Digite um número: '))
tot = 0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[32m')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')
print('\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
