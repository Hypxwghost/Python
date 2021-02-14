d_romanos = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}

i_inteiro = int()
s_romano = input('Número romano: ')

l_romano = [d_romanos[letra] for letra in s_romano]

for id, num in enumerate(l_romano):
    try:
        if num < l_romano[id+1]:
            i_inteiro -= num
        else:
            i_inteiro += num
    except:
        i_inteiro += num
    
print(i_inteiro)