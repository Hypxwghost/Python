import os
import platform
import tkinter.ttk as ttk

from tkinter import *
from tkinter import filedialog

# Prints connected drives Ex: 'C:' 'D:' ...
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]
print(drives)

root = Tk()

def listDir():
    listdir = os.listdir(os.getcwd())

    for x in listdir:
        print(x)

def cd(dir):   
    try:
        os.chdir(f'{dir}' + '\\')
        listDir()
    except:
        print("file/dir not found")

def openFile(file):
    #if file.endswith('.txt'):
    try:
        txt_edit = 'code'

        text_files = ['.txt', '.py', '.c', '.cs', '.md', '.rs']

        if file.endswith(text_files):
            with open(file, 'r') as file:
                os.system(f'{txt_edit} {file}')

    except FileNotFoundError:
        print("File not found")

while True:
    user_input = input('> ')
    if user_input[0:2] == 'cd':
        dir = user_input[3:]
        if len(dir) > 0:
            cd(dir)

    elif user_input[0:3] == 'cat':
        openFile(user_input[4:])

root.mainloop()
