import threading
from tkinter import *
import tkinter as tk
import win32api
import win32gui
import pyautogui
import my_keyboard
from time import sleep
from PIL import Image, ImageTk
from actions import minigame, set_fishing_rod, wait_bubble, use_potions, catch_pokes
import globals

# running = False


def catcher_shiny():
    if b4_var.get() == 1:
        globals.catcher_shiny = True
    else:
        globals.catcher_shiny = False


def use_potions_mark():
    if b3_var.get() == 1:
        globals.use_potions = True
        use_potions()
    else:
        globals.use_potions = False


def bot():
    globals.running = True
    handle = win32gui.FindWindow(None, "PokeXGames")
    win32gui.SetForegroundWindow(handle)
    while globals.running:
        fishing_position = set_fishing_rod()
        wait_bubble(fishing_position)
        minigame()
        my_keyboard.press("f11")
        sleep(1)


def stop_bot():
    globals.running = False


def photo(x, y):
    screen_shot = pyautogui.screenshot(region=(x - 35, y - 35, 70, 70))
    screen_shot.save("bolhas.png")
    new_image = Image.open("bolhas.png")
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo


def enable_mouseposition():
    window.iconify()
    window.after(10, get_mouseposition)


def get_mouseposition():
    state_left = win32api.GetKeyState(0x01)
    if state_left == -127 or state_left == -128:
        xclick, yclick = map(int, win32api.GetCursorPos())
        photo(xclick, yclick)
        window.deiconify()
        window.attributes("-topmost", True)
        label.update()
    else:
        window.after(10, get_mouseposition)


def start_bot_thread():
    thread = threading.Thread(target=bot)
    thread.daemon = True  # Configura a thread como um daemon para que ela seja interrompida quando o programa for encerrado
    thread.start()


def use_potions_thread():
    thread = threading.Thread(target=use_potions_mark)
    thread.daemon = True  # Configura a thread como um daemon para que ela seja interrompida quando o programa for encerrado
    thread.start()


def use_catcher_thread():
    thread = threading.Thread(target=catcher_shiny)
    thread.daemon = True  # Configura a thread como um daemon para que ela seja interrompida quando o programa for encerrado
    thread.start()


window = Tk()
window.title("Testing")
image = Image.open("bolhas.png")
foto = ImageTk.PhotoImage(image)
label = Label(window, image=foto)
label.grid(row=1, column=3, sticky=W)
label.config(image=foto)

b3_var = IntVar()
b4_var = IntVar()

b = Button(window, text="Tire a ScreenShot das BOLHAS", command=enable_mouseposition)
b.grid(row=0, column=0, sticky=W)

b1 = Button(window, text="Start BOT", command=start_bot_thread)
b1.grid(row=1, column=0, sticky=W)

b2 = Button(window, text="Stop BOT", command=stop_bot)
b2.grid(row=2, column=0, sticky=W)

b3 = Checkbutton(
    window,
    text="Use Potions",
    variable=b3_var,
    onvalue=1,
    offvalue=0,
    command=use_potions_thread,
)
b3.grid(row=3, column=0, sticky=tk.W)

b4 = Checkbutton(
    window,
    text="Use Catcher Shiny",
    variable=b4_var,
    onvalue=1,
    offvalue=0,
    command=use_catcher_thread,
)
b4.grid(row=3, column=1, sticky=tk.W)

desired_width = (
    b.winfo_reqwidth()
    + label.winfo_reqwidth()
    + b1.winfo_reqwidth()
    + b2.winfo_reqwidth()
)
desired_height = (
    b.winfo_reqheight()
    + label.winfo_reqheight()
    + b1.winfo_reqheight()
    + b2.winfo_reqheight()
)
window.geometry("{}x{}".format(desired_width, desired_height))
window.mainloop()
