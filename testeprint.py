import os
import glob
import my_keyboard
import pyautogui
import keyboard
from time import sleep

REGION_CAP = 838, 327, 223, 221


def catch_pokes():
    path = r'C:\Users\Sockz\OneDrive\Área de Trabalho\PXG\images'
    path = os.path.realpath(path)
    os.chdir(path)
    lista_pokes = os.listdir()
    for pokes in lista_pokes:
        pokemorto = pyautogui.locateOnScreen('{0}'.format(pokes),confidence=0.95,region=REGION_CAP)
        if pokemorto != None:
            print(pokemorto)
            pokemon_x, pokemon_y = pyautogui.center(pokemorto)
            pyautogui.moveTo(pokemon_x, pokemon_y)
            my_keyboard.pressi('f9')
keyboard.wait('~')
while True:
    catch_pokes()
    sleep(10)
    print("sucesso")
    
