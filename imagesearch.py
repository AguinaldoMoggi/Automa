import pyautogui
from time import sleep
import keyboard

keyboard.wait('k')
while True:
    battle = pyautogui.locateOnScreen("Battle.png",confidence=0.8)
    print(battle)
    sleep(5)
