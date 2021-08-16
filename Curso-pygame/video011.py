class Cachorro:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho

    def latir(self):
        print('au')

    def correr(self):
        print(f'{self.nome} está correndo')


cachorro1 = Cachorro('Toby', 'marrom', 5, 'grande')

# print(cachorro1.nome)
# print(cachorro1.idade)
# cachorro1.idade = 8
# print(cachorro1.idade)

cachorro1.latir()
cachorro1.correr()

cachorro2 = Cachorro('Max', 'preto', 3, 'pequeno')
print(cachorro2.tamanho)
