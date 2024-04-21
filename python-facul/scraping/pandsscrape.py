import requests
import pandas as pd
from bs4 import BeautifulSoup

txt_str = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
bsp_texto = BeautifulSoup(txt_str, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})
dados = []

for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017'
    comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])
print(df_noticias.shape)
print(df_noticias.dtypes)
print("-")
print(df_noticias.head())
