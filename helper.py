from tkinter import *
import win32api
import pyautogui
from PIL import Image, ImageTk
from time import sleep

global_area = None
boia_size = (70, 70)


def on_resize(event):
    print()


def mouseMove():
    global global_area
    print(global_area)
    if global_area is not None:
        pyautogui.moveTo(global_area)


def photo(x, y):
    screen_shot = pyautogui.screenshot(region=(x - 35, y - 35, 70, 70))
    screen_shot.save("testecapcoord.png")
    new_image = Image.open("testecapcoord.png")
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo
    while True:
        boiateste = pyautogui.locateOnScreen("testecapcoord.png", confidence=0.8)
        if boiateste != None:
            break
    area = pyautogui.center(boiateste)
    global global_area
    global_area = area


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


window = Tk()

window.title("Testing")
image = Image.open("testecapcoord.png")
foto = ImageTk.PhotoImage(image)
label = Label(window, image=foto)
label.grid(row=1, column=3, sticky=W)
label.config(image=foto)

b = Button(window, text="Tire a ScreenShot das BOLHAS", command=enable_mouseposition)
b.grid(row=0, column=2, sticky=W)

b1 = Button(window, text="teste", command=mouseMove)
b1.grid(row=0, column=3, sticky=W)

desired_width = b.winfo_reqwidth() + label.winfo_reqwidth()
desired_height = b.winfo_reqheight() + label.winfo_reqheight()
window.geometry("{}x{}".format(desired_width, desired_height))
window.mainloop()
