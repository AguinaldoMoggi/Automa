import pyautogui
from my_keyboard import key_down, release_key
import my_keyboard
import button

REGIAO = 948, 489, 44, 365


def minigame():
    while True:
        peixe = pyautogui.locateOnScreen("peixe1.png", confidence=0.80, grayscale=True)
        barra = pyautogui.locateOnScreen("barra2.png", confidence=0.80, region=REGIAO)
        if barra.top > peixe.top:
            key_down(0x39)
        else:
            release_key(0x39)