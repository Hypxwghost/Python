def executar_selection_sort(lista):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

def executar_selection_sort_2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada

def executar_bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def executar_insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        valor_inserir = lista[i]
        j = i -1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j+1] = valor_inserir
    return lista

lista = [10, 9, 5, 8, 11, -1, 3]
# print(executar_selection_sort(lista))
# print(executar_selection_sort_2(lista))
# print(executar_bubble_sort(lista))
print(executar_insertion_sort(lista))