import keyboard
import pyautogui
import time
import cv2
import numpy as np

# Load the template image you want to match
template = cv2.imread('aim.PNG')

# Define the screen area to search in (left, top, width, height)
area = (140, 260, 1340, 800)

# Function to find and click on the template match
def find_and_click_template(template):
    screen = np.array(pyautogui.screenshot(region=area))
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # You can adjust the threshold value as needed
    threshold = 0.1
    if max_val >= threshold:
        click_x, click_y = max_loc
        h, w, _ = template.shape
        click_location(click_x + w // 2, click_y + h // 2)
        return True
    else:
        return False

# Function to click on a specific location
def click_location(x, y):
    pyautogui.click(x + area[0], y + area[1])

def stop_program(e):
    global running
    running = False

keyboard.on_press_key('esc', stop_program)

running = True
while running:
    find_and_click_template(template)


keyboard.unhook_all()