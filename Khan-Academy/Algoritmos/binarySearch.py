from math import floor

def binarySearch(array, alvo):
    n = len(lista)
    min = count = 0
    max = n-1    

    while True:
        count += 1 # contador
        
        # se o max for menor que min,o numero não está no array, retorna -1
        if max < min: 
            print('Não está no array!')
            return -1

        chute=floor((min+max)/2) # calcula o "chute" ou "guess"

        # se o chute for igual ao alvo,o programa para e mostra informações
        if lista[chute] == alvo: 
            print(f'\nO numero alvo é: {alvo}')
            print(f"O index onde o número se encontra é: {chute}")
            print(f"Encontrado apos {count} iterações")
            break

        if lista[chute] < alvo:
            min = chute + 1

        if lista[chute] > alvo:
            max = chute - 1

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
numbers_user = []

while True:
    try:
        print('-'*30)
        escolha = int(input("Lista padrão[1] ou lista customizada?  "))
        break
    except ValueError:
        print('Escolha inválida')        

while True:            
    if escolha == 1:
        lista = numbers
        break
    
    else:
        try:
            # escolhe a lista e guarda os numeros do usuario
            lista = numbers_user

            print('-'*30)
            num = int(input('''Digite um número para a lista 
            --> ordem crescente <-- 
            [996699 - Sair]:  '''))
            print('-'*30)

            if num == 996699:
                break

            numbers_user.append(num)

            print(f'Lista: {numbers_user}')
        except ValueError:
            print('Digite apenas númeos válidos!')

print('-'*30)
print(f"--> Lista final: {lista} <--")
print('-'*30)

num_alvo = int(input('Digite o número alvo: '))

# inicia a procura
binarySearch(lista, num_alvo)