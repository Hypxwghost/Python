import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests

class ExtracaoPortal:
    def __init__(self):
        self.portal = None
    
    def extrair(self, portal):
        self.portal = portal
        txt_str = requests.get('https://globoesporte.globo.com/').text
        hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        bsp_texto = BeautifulSoup(txt_str, 'html.parser')
        lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
        dados = []

        for noticia in lista_noticias:
            pr_man = noticia.contents[1].text.replace('"',"")
            url = noticia.find('a')['href']
            desc = noticia.contents[2].text

            if not desc:
                desc = noticia.find('div', attrs={'class': 'bstn-related'})
                desc = desc.text if desc else None

            metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
            secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})
            secao = secao.text if secao else None

            time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
            time_delta = time_delta.text if time_delta else None

            dados.append((pr_man, desc, url, secao, hora_extracao, time_delta))
        df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
        return df
    
df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
print(df.head())