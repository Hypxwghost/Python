import getpass

while True:
    try:
        login = input('Digite o nome de usuario: ').upper()
        senha = int(getpass.getpass('Digite a senha: '))

        if login == 'GHOSTE' and senha == 1234:
            print(f'Bom dia {login},seu acesso foi autorizado!')
            break
        else:
            print('Acesso negado!')
    except TypeError:
        print('Digite apenas númeoros na senha !!')