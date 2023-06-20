import pyautogui
from time import sleep
import keyboard
from tkinter import *

def getpos():
    janela.after(10, leftclickpos)


def leftclickpos():
    xclicl, yclick= pyautogui.position()
    print(xclicl, yclick)




janela = Tk()
frame = Frame(janela, width=200, height=100)
janela.bind("<Button-1>", getpos)
janela.title("testando")
texto_teste = Label(janela, text="testando botao")
texto_teste.grid(column=0, row=0)
botao = Button(janela, text="Escolha a coordenada", command=getpos)
botao.grid(column=1, row=1)
janela.mainloop()

# while True:
#     karpao = pyautogui.locateOnScreen("karpao.png")
#     x_karpao, y_karpao = pyautogui.center(karpao)
#     print(karpao)
#     sleep(5)
    
#     keyboard.wait('p')
#     pos = getpos()
#     sleep(5)
#     pyautogui.moveTo(pos)

