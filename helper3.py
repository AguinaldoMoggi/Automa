import tkinter as tk
import pyautogui
import win32api
from PIL import Image, ImageTk

class Watermark:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()
        self.canvas.bind('<Motion>', self.update_position)
        self.watermark = self.canvas.create_text(0, 0, text='MARCA d\'AGUA', fill='red', font=('Arial', 12))
        self.visible = False


    def update_position(self, event):
        if self.visible:
            self.canvas.coords(self.watermark, event.x, event.y)

    def show(self):
        self.visible = True
        self.canvas.lift(self.watermark)

    def hide(self):
        self.visible = False
        self.canvas.lower(self.watermark)

def photo(x, y):
    screen_shot = pyautogui.screenshot(region=(x-35, y-35, 70, 70))
    screen_shot.save('teste.png')
    new_image = Image.open("teste.png")
    new_photo = ImageTk.PhotoImage(new_image)
    label.config(image=new_photo)
    label.image = new_photo

def get_mouseposition():
    state_left = win32api.GetKeyState(0x01)
    if state_left == -127 or state_left == -128:
        xclick, yclick = map(int, win32api.GetCursorPos())
        photo(xclick, yclick)
        watermark.canvas.coords(watermark.watermark, xclick, yclick)
        watermark.show()
    else:
        watermark.hide()
        window.after(10, get_mouseposition)

def enable_mouseposition():
    window.iconify()
    window.after(10, get_mouseposition)

root = tk.Tk()
watermark = Watermark(root)
button = tk.Button(root, text='Selecionar Região', command=get_mouseposition)
button.pack()
window = tk.Toplevel(root)
label = tk.Label(window, text='Hello, World!')
label.pack()
window.withdraw()
root.mainloop()
