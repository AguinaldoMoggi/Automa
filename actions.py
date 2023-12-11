import glob
import time
from tkinter import messagebox
import tkinter as tk
import pyautogui
import keyboard
import my_keyboard
from time import sleep
import random
import os
import globals
import os
import sys
import json


# (1421, 397)
# 1465 515
REGIAO_POT = (10, 109, 151, 30)
FISH_POSITION = ''
FISH_SIZE = (90, 90)
BOIA_SIZE = (20, 20)
MINIGAME_REGION = (939, 492, 37, 354)
REGION_TESTE = 7, 108, 35, 75
REGION_CAP = 838, 327, 223, 221
RGB_GREEN = (0, 145, 0)
RGB_LIGHT_GREEN = (62, 124, 62)
RGB_YELLOW = (124, 124, 0)
RGB_RED = (148, 8, 8)
RGB_NO_MONSTERS = (7, 9, 12)
X_LIFE = 49
Y_LIFE = 129
X_NO_MONSTERS = 25
Y_NO_MONSTERS = 152

HOTKEYS = ['DESLIGADO','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']
ATTACK_LIST = ['F1','F2','F3','F4','F5','F6','F7','F8']
data = ''

if data != '':
    with open('infos.json', 'r') as file:
        data = json.loads(file.read())



def use_potions():
    while globals.use_potions:
        enable_pot = pyautogui.pixelMatchesColor(X_LIFE, Y_LIFE, RGB_YELLOW or RGB_RED)
        no_pokes = pyautogui.pixelMatchesColor(
            X_NO_MONSTERS, Y_NO_MONSTERS, RGB_NO_MONSTERS
        )
        if enable_pot is True and no_pokes is True:
            my_keyboard.press(globals.hotkey_potion)
            sleep(1)
        heal_with_pokes = pyautogui.pixelMatchesColor(X_LIFE, Y_LIFE, RGB_RED)
        if heal_with_pokes is True:
            my_keyboard.press(globals.hotkey_potion)


def catch_pokes():
    previous_directory = os.getcwd()
    
    current_directory = os.path.abspath(os.path.dirname(__file__))
    path_principal = os.path.join(current_directory, 'images')
    
    # path_principal = r"C:\Users\Sockz\OneDrive\Área de Trabalho\PXG\images"
    os.chdir(path_principal)
    poke_list = os.listdir(path_principal)
    
    for poke in poke_list:
        pokemorto = pyautogui.locateOnScreen(
            "{0}".format(poke), confidence=0.95, region=REGION_CAP
        )
        if pokemorto is not None:
            pokemon_x, pokemon_y = pyautogui.center(pokemorto)
            pyautogui.moveTo(pokemon_x, pokemon_y)
            my_keyboard.press(globals.hotkey_pokeball)
            time.sleep(1)
    # path = r"C:\Users\Sockz\OneDrive\Área de Trabalho\PXG"
    path = os.path.join(current_directory, '..')
    os.chdir(previous_directory)


def set_fishing_rod():
    area = tuple(FISH_POSITION)
    center_area = pyautogui.center(area + FISH_SIZE)
    pyautogui.moveTo(center_area)
    sleep(0.5)
    my_keyboard.press(globals.hotkey_varinha)
    sleep(2)
    return area


def wait_bubble(fish_position):
    while globals.running:
        boia = pyautogui.locateOnScreen("boia.png", confidence=0.8, region=fish_position + FISH_SIZE)
        bolhas = pyautogui.locateOnScreen(
            "bolhas.png", confidence=0.8, region=fish_position + FISH_SIZE
        )
        poke_allright = pyautogui.pixelMatchesColor(
            X_LIFE, Y_LIFE, RGB_RED or RGB_YELLOW
        )
        poke_off_ball = pyautogui.pixelMatchesColor(X_LIFE, Y_LIFE, RGB_NO_MONSTERS)
        
        if boia == None:
            print(boia) 
            set_fishing_rod()
        else: 
            if bolhas != None:
                if poke_allright is not True and poke_off_ball is not True:
                    my_keyboard.press(globals.hotkey_varinha)
                    break
        if globals.catcher_shiny:
            catch_pokes()

def attack_spells():
    sleep(2)
    poke = pyautogui.locateOnScreen("shinystar.png", confidence=0.8, region=[3, 50, 199, 165])
    pyautogui.click(poke)
    while poke:
        for attack in ATTACK_LIST:
            poke = pyautogui.locateOnScreen("shinystar.png", confidence=0.8, region=[3, 50, 199, 165])
            if (poke):
                my_keyboard.press(attack)
                sleep(2)

def minigame():
    sleep(1)
    peixe = True
    while peixe != None:
        barra = pyautogui.locateOnScreen(
            "barra5.png", confidence=0.8, region=MINIGAME_REGION
        )
        peixe = pyautogui.locateOnScreen(
            "peixe1.PNG", confidence=0.8, region=MINIGAME_REGION, grayscale=True
        )
        if barra != None and peixe != None:
            if barra.top > peixe.top:
                my_keyboard.key_down(0x39)
            else:
                my_keyboard.release_key(0x39)
        else:
            my_keyboard.key_down(0x39)
            my_keyboard.release_key(0x39)

def procurar_imagem():
    global busca_ativa
    busca_ativa = True
    while busca_ativa:
        global FISH_POSITION
        try:
            image_location = pyautogui.locateOnScreen('boia.png', confidence=0.8)
            if image_location is not None:
                x, y, _, _ = image_location  # Ignorando os outros dois valores retornados
                center_x = x - 40
                center_y = y - 35
                FISH_POSITION = center_x, center_y
                busca_ativa = False
                messagebox.showinfo(title="Coordenadas da Boia!", message=f"Coordenadas: x={x}, y={y}")
        except:
            pass
        
def reiniciar_programa():
    python = sys.executable
    os.execl(python, python, "botComInterface.py", *sys.argv)