try:
        import time
        import pyautogui
        import datetime
except:
        print("An error occured.")
        print("A package failed to load.")
        print("pyautogui is likely missing. Run setup.bat. If that doesent work, try executing from comandline")
        print("with 'python main.py' do not use 'main.py', as this seems to cause this.")
        print("Exiting in 60 seconds.")
        time.sleep(60)
        print("Exiting....")
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
