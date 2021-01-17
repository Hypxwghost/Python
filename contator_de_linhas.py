import os
import sys
from time import sleep

linhas_cont_py = file_cont_py = linhas_cont_md = file_cont_md = linhas_cont_txt = file_cont_txt = linhas_cont_c = file_cont_c = linhas_cont_html = file_cont_html = linhas_cont_css = file_cont_css = linhas_cont_js = file_cont_js = 0

caminho = os.path.dirname(os.path.realpath(__file__))
print(f'Pegando arquivos em: {caminho}')
sleep(2)

for root, dirs, files in os.walk(caminho):
    for file in files:
        if file.endswith('md'): # Makrdown
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_md += 1
                script_code = f.readlines()
            
            for line in script_code:
                linhas_cont_md += 1

        if file.endswith('.py'): # Python
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_py += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_py += 1

        if file.endswith('.txt'): # Text
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_txt += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_txt += 1

        if file.endswith('.c'): # C
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_c += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_c += 1

        if file.endswith('.html'): # html
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_html += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_html += 1

        if file.endswith('.css'): # css
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_css += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_css += 1

        if file.endswith('.js'): # js
            with open(root+'/'+str(file), 'r', errors='ignore') as f:
                file_cont_js += 1
                script_code = f.readlines()

            for line in script_code:
                linhas_cont_js += 1
                
# Solução temporaria,ate eu achar uma melhor ._.

if linhas_cont_py != 0:
    print(f'Você tem {linhas_cont_py} linhas de codigo em {file_cont_py} arquivos .py')
if linhas_cont_md != 0:
    print(f'Você tem {linhas_cont_md} linhas em {file_cont_md} arquivos .md')
if linhas_cont_txt != 0:
    print(f'Você tem {linhas_cont_txt} linhas em {file_cont_txt} arquivos .txt')
if linhas_cont_c != 0:
    print(f'Você tem {linhas_cont_c} linhas em {file_cont_c} arquivos .c ')
if linhas_cont_html != 0:
    print(f'Você tem {linhas_cont_html} linhas em {file_cont_html} arquivos .html')
if linhas_cont_css != 0:
    print(f'Você tem {linhas_cont_css} linhas em {file_cont_css} arquivos .css')
if linhas_cont_js != 0:
    print(f'Você tem {linhas_cont_js} linhas em {file_cont_js} arquivos .js')
