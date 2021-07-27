import socket
import threading
import tkinter.ttk as ttk

from tkinter import *
from getpass import getpass
from datetime import datetime

stop_thread = False

win = Tk()
win.title("TcpChatRoom")
text = StringVar()

entry = ttk.Entry(win, textvariable=text)
entry.pack()
#entry.grid(row=0, columnspan=2)


def serverConnect(ip, port):
    client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

def getMsg():
    response = entry.get()
    if len(response) <= 0:
        pass
    else:
        return response

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

label = Label( win, textvariable=text, relief=RAISED )

text.set("Nickname: ")
label.pack()

nickname = getMsg()

print(nickname)

# serverConnect('127.0.0.1', 55555)


button_send = ttk.Button(win, text=">", command=getMsg)
button_send.pack()
#button_send.grid(row=0, column=3)

win.mainloop()

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=getMsg)
write_thread.start()