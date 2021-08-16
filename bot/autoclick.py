import time

import keyboard
import pyautogui

time.sleep(5)  # Tempo de espera(5 segundos)
f = 0
while f == 0:
    pyautogui.press('1', interval=0.05)
    if keyboard.is_pressed('esc'):
        break
