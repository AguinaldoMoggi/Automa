import pyautogui
from my_keyboard import key_down, release_key
REGIAO = 948, 489, 44, 365

while True:
    peixe = pyautogui.locateOnScreen("peixe1.png", confidence=0.80, grayscale=True)
    barra = pyautogui.locateOnScreen("barra2.png", confidence=0.80, region=REGIAO)
    if peixe != None and barra != None:
        if barra.top > peixe.top:
            key_down(0x39)
        else:
            release_key(0x39)