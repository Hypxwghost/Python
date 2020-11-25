# script para calcular o valor de delta
def raizes(a, b, c):
    d = (b ** 2 - 4 * a * c)
    print("O valor de delta é igual a {}".format(d))


if __name__ == '__main__':
    while True:
        a = float(input('Entre com o valor de a: '))
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
        raizes(a, b, c)

        continua = input('Q -sair /n Enter -Continuar')
        if continua == 'q':
            break
