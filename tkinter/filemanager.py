import os

from tkinter import *

# Prints connected drives Ex: 'C:' 'D:' ...
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]
print(drives)

root = Tk()


def list_dir():
    listdir = os.listdir(os.getcwd())

    for x in listdir:
        print(x)


def cd(directory):
    try:
        os.chdir(f'{directory}' + '\\')
        list_dir()
    except:
        print("file/directory not found")


def open_file(file):
    # if file.endswith('.txt'):
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
        directory = user_input[3:]
        if len(directory) > 0:
            cd(directory)

    elif user_input[0:3] == 'cat':
        open_file(user_input[4:])

root.mainloop()
