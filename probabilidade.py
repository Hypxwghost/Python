# calculo de probabilidade
def fatorial(num):
	fatorial = 1
	while num > 0:
		fatorial *= num
		num -= 1
	return fatorial
	
dividendo = fatorial(365)
divisor = fatorial(335) * 365 ** 30

print(str(1-dividendo/divisor)[:5])