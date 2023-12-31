from tkinter import *
import win32api


def enable_mouseposition():
    window.after(10, get_mouseposition)
    window.iconify()
    


def get_mouseposition():
    state_left = win32api.GetKeyState(0x01)
    if state_left == -127 or state_left == -128:
        xclick, yclick = win32api.GetCursorPos()
        print(xclick, yclick)
        window.deiconify()
    else:
        window.after(10, get_mouseposition)

window = Tk()
window.geometry("300x300")
window.title("Testing")
window.focus()
# window.iconify()

b = Button(window, text="OK", command=enable_mouseposition)
b.grid(row=0, column=2, sticky=W)

window.mainloop()