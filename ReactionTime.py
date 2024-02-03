import pyautogui
import time

while True:
    if pyautogui.pixel(140, 260) == (75, 219, 106):
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()