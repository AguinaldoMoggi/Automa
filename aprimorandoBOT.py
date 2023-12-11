import threading
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Label, Button, Checkbutton
from ttkthemes import ThemedTk
import win32api
import win32gui
import pyautogui
import my_keyboard
from time import sleep
from PIL import Image, ImageTk
import actions
from actions import minigame, set_fishing_rod, wait_bubble, use_potions, catch_pokes, procurar_imagem, reiniciar_programa, FISH_POSITION
import globals
import json
import numpy as np


class GuiBot:
    def __init__(self):
        self.window = ThemedTk(theme="black", themebg=True)
        self.window.title("Gui-BOT")
        # ... outros widgets

        self.image_bolhas = Image.open("1bolhas.png")
        self.foto_bolhas = ImageTk.PhotoImage(self.image_bolhas)
        self.label = Label(image=self.foto_bolhas)
        self.label.grid(row=1, column=3, sticky='W')
        self.label.config(image=self.foto_bolhas)

        # ... outros widgets

        self.teste = self.gerador_widget(Button, row=0, column=0, sticky="w", text="testando")
        self.btn = self.gerador_widget(Button, row=1, column=1, sticky="w", text="BTN 1", command=lambda: self.printar("Eu sou legal"))
        self.cbx = self.gerador_widget(Combobox, row=2, column=0, sticky="w", values=actions.HOTKEYS, state='readonly', width=9)
        self.cbx.current(0)
        self.testebtnphoto = self.gerador_widget(Button, row=3, column=0, sticky="w", text="Button Photo", command=self.enable_mouseposition)

    def gerador_widget(self, widget, row, column, sticky="NSEW", columnspan=None , **kwargs):
        my_widget = widget(**kwargs)
        my_widget.grid(row=row, column=column, padx= 5, pady= 5, columnspan=columnspan,sticky=sticky)
        return my_widget

    def enable_mouseposition(self):
        messagebox.showinfo(title="Selecione as bolhas!", message="Click sobre as bolhas!!!")
        self.window.iconify() 
        self.window.after(10, self.get_mouseposition)
        
    def get_mouseposition(self):
        state_left = win32api.GetKeyState(0x01)
        if state_left == -127 or state_left == -128:
            xclick, yclick = map(int, win32api.GetCursorPos())
            self.photo(xclick, yclick)
            self.window.deiconify()
            self.window.attributes("-topmost", True)
            self.label.update()
        else:
            self.window.after(10, self.get_mouseposition)
                
    def photo(self, x, y):
        self.screen_shot = pyautogui.screenshot(region=(x - 30, y - 30, 60, 60))
        self.screen_shot.save("1bolhas.png")
        self.new_image_bolhas = Image.open("1bolhas.png")
        self.new_photo_bolhas = ImageTk.PhotoImage(self.new_image_bolhas)
        self.label.config(image=self.new_photo_bolhas)
        self.label.image = self.new_photo_bolhas

    def start_bot_thread(self):
        thread = threading.Thread(target=self.bot)
        thread.daemon = True
        thread.start()

    def bot(self):
        globals.running = True
        handle = win32gui.FindWindow(None, "PokeXGames")
        win32gui.SetForegroundWindow(handle)
        while globals.running:
            fishing_position = set_fishing_rod()
            wait_bubble(fishing_position)
            minigame()
            my_keyboard.press("f11")
            sleep(1)

if __name__ == "__main__":
    gui_bot = GuiBot()
    gui_bot.window.mainloop()
