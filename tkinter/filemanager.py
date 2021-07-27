import os
import platform
import tkinter.ttk as ttk
from tkinter import *

tk = Tk()

drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

print(drives)

def getDir():
    listdir = os.listdir(os.getcwd())

    list_lbl = Label(tk, text='a')
    list_lbl.pack()

    for x in listdir:
        print(x)

def cd():
    os.chdir('C:' + '\\')
    getDir()

tk.mainloop()
