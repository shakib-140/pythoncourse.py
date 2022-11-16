import pyautogui
import time
#pyautogui.alert('This is an alert box.')
#time.sleep(10)
for i in range(1,5):
 time.sleep(2)
 pyautogui.write('i love you!', interval=0.25)
 pyautogui.press('enter')

