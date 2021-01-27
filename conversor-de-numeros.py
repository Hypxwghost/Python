nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
num2 = []

cont1 = cont5 = cont10 = cont50 = cont100 = cont500 = cont1000 =  0

num = input('Digite um número romano: ').upper()

for num in num:
    if num == 'I':
        cont1 += 1

    elif num == 'V':
        cont5 += 1

    elif num == 'X':
        cont10 += 1

    elif num == 'L':
        cont50 += 1

    elif num == 'C':
        cont100 += 1

    elif num == 'D':
        cont500 += 1

    elif num == 'M':
        cont1000 += 1

print(cont1, cont5, cont10, cont50, cont100, cont500, cont1000)