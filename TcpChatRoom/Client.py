import socket
import threading
from datetime import datetime
from getpass import getpass

# Choosing nickname
nickname = input('Choose your nickname: ')
if nickname == 'admin':
    password = getpass('Enter password for admin: ')

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# variables
stop_thread = False


# Gets actual time
def actualTime():
    now = datetime.now()
    nowf = now.strftime('%H:%M:%S')
    return nowf


# listening to server and sending nickname
def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            # Receive message from server
            # if "NICK" send nickname
            message = client.recv(1024).decode('ascii')

            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')

                if next_message == 'PASS':
                    client.send(password.encode('ascii'))

                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print('Connection was refused!')
                        stop_thread = True

                elif next_message == 'BAN':
                    print('Connection refused because of ban!')
                    client.close()
                    stop_thread = True

            else:
                print(f"{actualTime()}: {message}")

        except:
            # close connection when error
            print('An error occurred!')
            client.close()
            break


# sending message to server
def write():
    while True:
        if stop_thread:
            break
        else:
            message = f'{nickname}: {input("> ")}'

            if message[len(nickname) + 2:].startswith('/'):
                if nickname == 'admin':
                    if message[len(nickname) + 2:].startswith('/kick'):
                        client.send(f'KICK {message[len(nickname) + 2 + 6:]}'.encode('ascii'))

                    elif message[len(nickname) + 2:].startswith('/ban'):
                        client.send(f'BAN {message[len(nickname) + 2 + 5:]}'.encode('ascii'))
                else:
                    print('Commands can only be executed by the admin!')
            else:
                client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
