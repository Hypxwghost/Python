import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0',60001))

quit = ['!QUIT','!Quit','!quit','!EXIT','!Exit','!exit']

on = True


def receive():
    on = True
    while on:
        try:
            message_server = client.recv(1024).decode('ascii')
            if message_server == 'NICK':
                print('nick trigger', type(message_server), message_server)
                client.send(nickname.encode('ascii'))
            elif message_server == 'QUIT':
                on = False
            else:
                print(message_server)
        except:
            print('An error ocurred!')
            client.close()
            break


def write():
    while on:
        message = f'{input("")}'
        if message in quit:
            client.send('!QUIT'.encode('ascii'))
        else:
            print('message ', type(message))
            message = message.encode('ascii')
            print('message encoded: ', type(message))
            client.send(message)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
