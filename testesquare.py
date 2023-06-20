import tkinter as tk

# Função para atualizar a posição do quadrado
def update_square_position(event):
    square_size = 30
    square_x = event.x - square_size // 2
    square_y = event.y - square_size // 2
    canvas.coords(square, square_x, square_y, square_x + square_size, square_y + square_size)

# Inicializar a janela do Tkinter
window = tk.Tk()
window.title("Botão com quadrado transparente")

# Criar um Canvas para exibir o quadrado
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Criar o quadrado inicialmente fora da tela
square_size = 30
square_x = -square_size
square_y = -square_size
square = canvas.create_rectangle(square_x, square_y, square_x + square_size, square_y + square_size, fill="red", outline="blue")

# Função a ser chamada quando o botão for clicado
def button_clicked():
    print("Botão clicado!")

# Criar o botão
button = tk.Button(window, text="Clique aqui", command=button_clicked)
button.pack()

# Associar a função de atualização à movimentação do mouse no canvas
canvas.bind("<Motion>", update_square_position)

# Iniciar o loop principal do Tkinter
window.mainloop()