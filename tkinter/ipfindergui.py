import socket

from tkinter import *

from requests import get

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Ipfinder")
        self.msg["font"] = ("Calibri", "11", "italic")
        self.msg.pack()
        self.btn = Button(self.widget1)
        self.btn["text"] = "Get info"
        self.btn["font"] = ("Calibri", "9")
        self.btn["width"] = 10
        self.btn.bind("<Button-1>", self.getIp)
        self.btn.pack ()

    def getIp(self, event):
        if self.msg["text"] == "Ipfinder":
            hostname = f'Hostname: {socket.gethostname()}'
            local_ip = f'Local IP: {socket.gethostbyname(socket.gethostname())}'
            ip = get('https://api.ipify.org').text
            public_ip = f'Public IP: {ip}'
            self.msg["text"] = f"{hostname}\n {local_ip}\n  {public_ip}"
            self.btn.destroy()

root = Tk()
Application(root)
root.mainloop()