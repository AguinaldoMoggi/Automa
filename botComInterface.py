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
from actions import minigame, set_fishing_rod, wait_bubble, use_potions, catch_pokes, procurar_imagem, reiniciar_programa, FISH_POSITION, attack_spells
import globals
import json
import numpy as np



def catcher_shiny():
    if checkbox_catcher_shiny_var.get() == 1:
        globals.catcher_shiny = True
    else:
        globals.catcher_shiny = False


def use_potions_mark():
    if checkBox_use_potions_var.get() == 1:
        globals.use_potions = True
        use_potions()
    else:
        globals.use_potions = False
        

def save():
    actions.FISH_POSITION = np.array(actions.FISH_POSITION)  # Se for uma matriz numpy
    actions.FISH_POSITION = actions.FISH_POSITION.tolist()
    
    print("Conteúdo de FISH_POSITION antes de salvar no arquivo JSON:")
    print(actions.FISH_POSITION)
    # Convertendo para lista
    my_data = {
        "varinha": { 
            "value" : cbx_varinha_pesca.get(),
            "position" : cbx_varinha_pesca.current()
            },
        "potion": {
            "value" : cbx_potion.get(),
            "position" : cbx_potion.current()
        },
        "pokeball":{
            "value" : cbx_pokeball.get(),
            "position" : cbx_pokeball.current()
        },
        "fishing_pos": {
            "value": actions.FISH_POSITION
        }
    }
    print(actions.FISH_POSITION)
    with open('infos.json', 'w') as file:
        file.write(json.dumps(my_data))
        
    print("Dados salvos no arquivo JSON.")


def load():
    global FISH_POSITION
    with open('infos.json', 'r') as file:
        data = json.loads(file.read())
    cbx_varinha_pesca.current(data['varinha']['position'])
    cbx_potion.current(data['potion']['position'])
    cbx_pokeball.current(data['pokeball']['position'])
    globals.hotkey_varinha = data["varinha"]["value"]
    globals.hotkey_potion = data["potion"]["value"]
    globals.hotkey_pokeball = data["pokeball"]["value"]
    actions.FISH_POSITION = data["fishing_pos"]["value"]
    return data


def bot():
    globals.running = True
    handle = win32gui.FindWindow(None, "PokeXGames")
    win32gui.SetForegroundWindow(handle)
    while globals.running:
        if (pyautogui.locateOnScreen("shinystar.png", confidence=0.8, region=[3, 50, 199, 165]) == None):
            fishing_position = set_fishing_rod()
            wait_bubble(fishing_position)
            minigame()
            my_keyboard.press("f11")
            sleep(1)
        else:
            attack_spells()
            


def stop_bot():
    globals.running = False


def photo(x, y):
    screen_shot = pyautogui.screenshot(region=(x - 30, y - 30, 60, 60))
    screen_shot.save("bolhas.png")
    new_image_bolhas = Image.open("bolhas.png")
    new_photo_bolhas = ImageTk.PhotoImage(new_image_bolhas)
    label.config(image=new_photo_bolhas)
    label.image = new_photo_bolhas
    



def enable_mouseposition():
    messagebox.showinfo(title="Selecione as bolhas!", message="Click sobre as bolhas!!!")
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
    
def captura_coordenada_thread():
    window.iconify()
    pyautogui.sleep(1)
    thread = threading.Thread(target=procurar_imagem)
    thread.daemon = True
    thread.start()
    window.deiconify()
    

window = ThemedTk(theme="black", themebg=True)
window.title("Gui-BOT")

def gerador_widget(widget, row, column, sticky="NSEW", columnspan=None , **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx= 5, pady= 5, columnspan=columnspan,sticky=sticky)
    return my_widget

image_bolhas = Image.open("bolhas.png")
foto_bolhas = ImageTk.PhotoImage(image_bolhas)

label = Label(image=foto_bolhas)
label.grid(row=1, column=3, sticky='W')
label.config(image=foto_bolhas)

checkBox_use_potions_var = IntVar()
checkbox_catcher_shiny_var = IntVar()

btn_tirar_foto_bolhas = Button(text="Tire a ScreenShot das BOLHAS", command=enable_mouseposition)
btn_tirar_foto_bolhas.grid(row=0, column=0, sticky='W')

# btn_start_bot = gerador_widget(Button, row=1, column=0, sticky=W, text="Start Bot", command=start_bot_thread)
btn_start_bot = Button(text="Start BOT", command=start_bot_thread)
btn_start_bot.grid(row=1, column=0, sticky='W')

btn_stop_bot = Button(text="Stop BOT", command=stop_bot)
btn_stop_bot.grid(row=2, column=0, sticky='W')

checkBox_use_potions = Checkbutton(
    window,
    text="Use Potions",
    variable=checkBox_use_potions_var,
    onvalue=1,
    offvalue=0,
    command=use_potions_thread,
)
checkBox_use_potions.grid(row=3, column=0, sticky='W')

checkbox_catcher_shiny = Checkbutton(
    window,
    text="Use Catcher Shiny",
    variable=checkbox_catcher_shiny_var,
    onvalue=1,
    offvalue=0,
    command=use_catcher_thread,
)
checkbox_catcher_shiny.grid(row=3, column=1, sticky='W')

btn_procurar_imagem = Button(text="Procurar Imagem", command=captura_coordenada_thread)
btn_procurar_imagem.grid(row=1, column=1, sticky='W')

btn_reinicio_bot = Button(text="Reiniciar-teste", command=reiniciar_programa)
btn_reinicio_bot.grid(row=2, column=1, sticky='W')


lbl_varinha_pesca = gerador_widget(Label, row=7, column=0, sticky='w', text='Hotkey da Varinha')
cbx_varinha_pesca = gerador_widget(Combobox, row=8, column=0, sticky="w",text="ComboBox Varinha", values=actions.HOTKEYS, state='readonly', width=9)
cbx_varinha_pesca.current(0)
# cbx_varinha_pesca = Combobox(text="ComboBoxTESTE", values=actions.HOTKEYS, state="readonly", width=9)
# cbx_varinha_pesca.grid(row=4, column=0,sticky='W')

lbl_potion = gerador_widget(Label, row=9, column=0, sticky='W', text='Hotkey Potion')
cbx_potion = gerador_widget(Combobox, row=10, column=0, sticky='W',values=actions.HOTKEYS, state='readonly', width=9)
cbx_potion.current(0)

lbl_pokeball = gerador_widget(Label, row=7, column=1, sticky='w', text="Hotkey Pokeball")
cbx_pokeball = gerador_widget(Combobox, row=8, column=1, sticky='w', values=actions.HOTKEYS, state='readonly', width=9)
cbx_pokeball.current(0)

btn_save_configs = gerador_widget(Button, row=6, column=0, sticky='E', text='Save Config', command=save)
btn_load_configs = gerador_widget(Button, row=6, column=0, sticky='W', text='Load Config', command=load)






# desired_width = (
#     btn_tirar_foto_bolhas.winfo_reqwidth()
#     + label.winfo_reqwidth()
#     + btn_start_bot.winfo_reqwidth()
#     + btn_stop_bot.winfo_reqwidth()
# )
# desired_height = (
#     btn_tirar_foto_bolhas.winfo_reqheight()
#     + label.winfo_reqheight()
#     + btn_start_bot.winfo_reqheight()
#     + btn_stop_bot.winfo_reqheight()
#     + btn_procurar_imagem.winfo_reqheight()
# )
# window.geometry("{}x{}+750+450".format(desired_width, desired_height))
window.geometry("500x500+750+450")
window.mainloop()