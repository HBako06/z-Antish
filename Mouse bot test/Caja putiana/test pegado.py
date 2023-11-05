import pyautogui 
import time
import pyperclip3 as pc

time.sleep(0.5)
x = "27971427"
pc.copy(x)
pyautogui.doubleClick(208,352)
pyautogui.press('backspace')
#time.sleep(0.2)
pyautogui.typewrite(x)
print(x)