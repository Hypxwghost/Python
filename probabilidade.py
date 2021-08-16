# calculo de probabilidade
def fatorial(num):
    fat = 1
    while num > 0:
        fat *= num
        num -= 1
    return fat


dividendo = fatorial(365)
divisor = fatorial(335) * 365 ** 30

print(str(1 - dividendo / divisor)[:5])
