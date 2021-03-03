from math import floor
from random import randint

def binarySearch(array, alvo):
    n = len(numbers)
    min = 0
    max = n-1

    while True:
        if max < min:
            print('Não está no array!')
            return -1

        chute=floor((min+max)/2)

        if numbers[chute] == alvo:
            print(chute)
            break

        if numbers[chute] < alvo:
            min = chute + 1

        if numbers[chute] > alvo:
            max = chute - 1

numbers = [
            2, 3, 5, 7, 11, 13, 17, 
            19, 23, 29, 31, 37, 41, 
            43, 47, 53, 59, 61, 67, 
            71, 73, 79, 83, 89, 97
            ]


binarySearch(numbers, 73)