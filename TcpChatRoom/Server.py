import threading
import socket

host = '0.0.0.0' # localhost
port = 60001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
        for client in clients:
            print('message to all clients: ', type(message))
            client.send(message)
        

def handle(client):
    while True:
                message = client.recv(1024)
                print(message)
                if message.decode('ascii') == '!QUIT':
                    client.send('QUIT')
                    index = clients.index((client))
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast(f'{nickname} left the chat!'.encode('ascii'))
                    nicknames.remove(nickname)
                    break
                else:
                    index = clients.index((client))
                    nickname = nicknames[index]
                    broadcast(f'{nickname}: {message}')


def receive():
    while True:
        try:
            client, address = server.accept()
            print(f'Connected with {address}')

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname of the client is {nickname}!')
            broadcast(f'{nickname} joined the chat !'.encode('ascii'))
            client.send('Conected to the server!'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except KeyboardInterrupt:
            print('Server has been shutdown!')
            break

print('Server is listening..')
receive()