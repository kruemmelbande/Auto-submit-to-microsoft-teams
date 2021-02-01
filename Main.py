import pyautogui
import time
import datetime
print("Waiting untill pro gamer move")
x=0
while x==0:
        now=datetime.datetime.now()
        print("current time=", now.hour,":", now.minute,".", now.second)
        if now.hour==4 and now.minute==20:
                x=1
        else:
                time.sleep(1)
print("Im about to do, whats called a pro gamer move")
pyautogui.moveTo(1727, 85, duration=10)
pyautogui.click()
print("Nice")
