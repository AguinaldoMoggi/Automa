import pyautogui
from time import sleep

boia = pyautogui.locateOnScreen("boia.png",confidence=0.8)

print(boia)
sleep(5)
