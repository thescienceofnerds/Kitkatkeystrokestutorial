import keyboard
import time
import pyautogui

while True:
    if keyboard.is_pressed("up"):
        print("you pressed macro")
        pyautogui.press("down")
        pyautogui.typewrite("macro was activated")
    else:
        print("macro wasn't activated")
        time.sleep(0.01)