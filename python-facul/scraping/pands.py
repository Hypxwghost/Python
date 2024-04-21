import pandas as pd

lista_idades = [32, 22, 25, 29, 38]
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
nomes_dict = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

lista_tpl = list(zip(lista_nomes, cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas

def Separa():
    print(40*"-")

um = pd.Series(data=5) # Cria uma Series com o valor a
dois = pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes
tres = pd.Series(nomes_dict) # Cria uma Series com um dicionário
quatro = pd.Series(lista_nomes, index=cpfs)
cinco = pd.Series([10.2, -1, None, 15, 23.4])
seis = pd.DataFrame(lista_tpl, columns=['nome', 'cpfs', 'idade', 'email'])

print(um)
Separa()
print(dois)
Separa()
print(tres)
Separa()
print(quatro)
Separa()
print(quatro.loc['111.111.111-11'])
Separa()


print('Quantidade de linhas = ', cinco.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados', cinco.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', cinco.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', cinco.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?', cinco.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', cinco.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', cinco.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', cinco.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', cinco.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', cinco.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', cinco.describe()) # Exibe um resumo sobre os dados na Series

Separa()
print(seis)

