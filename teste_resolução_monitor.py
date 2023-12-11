import pyautogui

resolucao_1920x1080 = (1920, 1080)

def verificar_resolucao():
    largura, altura = pyautogui.size()
    resolucao = (largura, altura)
    if (resolucao == resolucao_1920x1080):
        print("LALALAL")
    return resolucao


import tkinter as tk
from tkinter import ttk

def printar(text):
    print(text)

def adicionar_aba(notebook, nome_aba=""):
    nova_aba = tk.Frame(notebook)
    notebook.add(nova_aba, text=nome_aba)
    return nova_aba

root = tk.Tk()
root.title("Exemplo de Abas")
root.geometry("500x500+750+450")

notebook = ttk.Notebook(root)

# Criando e adicionando uma primeira aba
aba_1 = adicionar_aba(notebook, "Aba 1")
label_aba1 = tk.Label(aba_1, text="Exemplo")
label_aba1.grid(row=0, column=0, padx=10, pady=10)




aba_2 = adicionar_aba(notebook, "Aba 2")

aba_2.grid_columnconfigure(0, weight=1)
aba_2.grid_rowconfigure(0, weight=0)

label_aba2 = tk.Label(aba_2, text="HOTKEYS")
label_aba2.grid(row=0, column=0, padx=5, pady=5)
label_aba2 = tk.Button(aba_2, text="Exemplo 1", command=lambda: printar("Oque eu quero fazer aqui"))
label_aba2.grid(row=1, column=0, sticky="W")
label_aba2 = tk.Button(aba_2, text="Exemplo 2", command=verificar_resolucao)
label_aba2.grid(row=2, column=0, sticky="w")
label_aba2 = tk.Button(aba_2, text="Exemplo 3")
label_aba2.grid(row=3, column=0, sticky="w")



notebook.pack(expand=True, fill="both")

root.mainloop()

