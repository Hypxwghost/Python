import pyautogui
import time
import keyboard
time.sleep(5)
f = open("loremv3.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    if keyboard.is_pressed('esc'):
        break
