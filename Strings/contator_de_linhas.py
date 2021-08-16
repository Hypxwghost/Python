import os
from time import sleep

linhas_cont_py = file_cont_py = linhas_cont_md = file_cont_md = linhas_cont_txt = file_cont_txt = linhas_cont_c = file_cont_c = linhas_cont_html = file_cont_html = linhas_cont_css = file_cont_css = linhas_cont_js = file_cont_js = 0

cont = 0

extension = ['.py', '.txt', '.md', '.js', '.html', '.css', '.c']

caminho = os.path.dirname(os.path.realpath(__file__))
print(f'Pegando arquivos em: {caminho}')
sleep(2)

for root, dirs, files in os.walk(caminho):
    for file in files:
        if file.endswith('md'):  # Makrdown
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_md += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_md += 1

        if file.endswith('.py'):  # Python
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_py += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_py += 1

        if file.endswith('.txt'):  # Text
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_txt += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_txt += 1

        if file.endswith('.c'):  # C
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_c += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_c += 1

        if file.endswith('.html'):  # html
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_html += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_html += 1

        if file.endswith('.css'):  # css
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_css += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_css += 1

        if file.endswith('.js'):  # js
            with open(root + '/' + str(file), 'r', errors='ignore') as f:
                file_cont_js += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_js += 1

lista = [
    [linhas_cont_py, file_cont_py],
    [linhas_cont_txt, file_cont_txt],
    [linhas_cont_md, file_cont_md],
    [linhas_cont_js, file_cont_js],
    [linhas_cont_html, file_cont_html],
    [linhas_cont_css, file_cont_css],
    [linhas_cont_c, file_cont_c]
]

for item in lista:
    cont += 1
    if item[1] > 0:
        print(f'Você tem {item[0]} linhas em {item[1]} arquivos {extension[cont - 1]}')
