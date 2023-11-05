import pyautogui

screenshot = pyautogui.screenshot()
print(screenshot.getpixel((1437, 405)))