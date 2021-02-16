num = int(input('Digite a quantidade de números: ')) + 1

with open('nums.txt', 'w+') as file:
    for x in range(1, num):
        file.write(str(x))
        file.write('\n')
