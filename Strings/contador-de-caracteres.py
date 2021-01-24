txt = input('Digite uma palavra/frase: ').strip().replace(' ', '')

char_list = [char for char in txt]
char_infos = list()

for char in list(dict.fromkeys(char_list)):
    char_infos.append([char, char_list.count(char)])

for item in char_infos:
    print(*item, sep=': ')
