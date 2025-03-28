import customtkinter as ctk
from frame import Frame_esquerdo, Frame_direito  # Importando as classes Frame_esquerdo e Frame_direito

# Criar a janela principal
root = ctk.CTk()

# Definir o tamanho da janela
root.geometry("900x600")  # Definindo a largura para 900 e altura para 600
root.title("Formulario DISC da empresa AFFIX FIDC")

# Bloquear o redimensionamento da janela
root.resizable(False, False)

# Usando grid para organizar os frames lado a lado
root.grid_columnconfigure(0, weight=1)  # Configurando a primeira coluna
root.grid_columnconfigure(1, weight=1)  # Configurando a segunda coluna

# Criar o frame esquerdo
frame_esquerdo = Frame_esquerdo(root, image_path="AFFIX(2).jpeg")
frame_esquerdo.grid(row=0, column=0, sticky="nsew")  # Usando grid para organizar o frame

# Criar o frame direito
frame_direito = Frame_direito(root)
frame_direito.grid(row=0, column=1, sticky="nsew")  # Usando grid para organizar o frame

# Iniciar o loop principal
root.mainloop()
