import customtkinter as ctk

class QuestFrame(ctk.CTkFrame):
    def __init__(self, master, nome, cpf, email, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Definir as dimensões fixas do frame_right
        self.width = 500  # Largura fixa
        self.height = 600  # Altura fixa

        # Criar o frame direito com fundo cinza
        self.frame_right = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color="grey")
        self.frame_right.grid(row=0, column=1, sticky="nsew")  # Usando grid para controlar o layout

        # Impedir que o frame mude de tamanho para se ajustar ao conteúdo
        self.frame_right.grid_propagate(False)  # Isso vai garantir que o frame não se ajuste ao conteúdo

       # Adicionar título ao Frame direito
        self.titulo = ctk.CTkLabel(self.frame_right, text="Questionario", font=("Arial", 24, "bold"))
        self.titulo.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.07)  # Título no topo

 # Bloco 1: "Você é feliz?" (Pergunta geral)
        self.label_quest1 = ctk.CTkLabel(self.frame_right, text="Você é feliz?")
        self.label_quest1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)

        # Opções de números para a pergunta geral (1 a 4)
        self.opcoes_quest1 = ["1", "2", "3", "4"]
        self.entry_quest1 = ctk.CTkOptionMenu(self.frame_right, values=self.opcoes_quest1)
        self.entry_quest1.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.05)

        # Bloco 2: "Em dias de sol?" (Pergunta complementar)
        self.label_quest2 = ctk.CTkLabel(self.frame_right, text="Em dias de sol?")
        self.label_quest2.place(relx=0.1, rely=0.17, relwidth=0.3, relheight=0.05)

        # Opções de números para a pergunta complementar 1 (1 a 4)
        self.entry_quest2 = ctk.CTkOptionMenu(self.frame_right, values=self.opcoes_quest1)
        self.entry_quest2.place(relx=0.5, rely=0.17, relwidth=0.1, relheight=0.05)

        # Bloco 3: "Em dias nublados?" (Pergunta complementar)
        self.label_quest3 = ctk.CTkLabel(self.frame_right, text="Em dias nublados?")
        self.label_quest3.place(relx=0.1, rely=0.24, relwidth=0.3, relheight=0.05)

        # Opções de números para a pergunta complementar 2 (1 a 4)
        self.entry_quest3 = ctk.CTkOptionMenu(self.frame_right, values=self.opcoes_quest1)
        self.entry_quest3.place(relx=0.5, rely=0.24, relwidth=0.1, relheight=0.05)

        # Bloco 4: "Em dias chuvosos?" (Pergunta complementar)
        self.label_quest4 = ctk.CTkLabel(self.frame_right, text="Em dias chuvosos?")
        self.label_quest4.place(relx=0.1, rely=0.31, relwidth=0.3, relheight=0.05)

        # Opções de números para a pergunta complementar 3 (1 a 4)
        self.entry_quest4 = ctk.CTkOptionMenu(self.frame_right, values=self.opcoes_quest1)
        self.entry_quest4.place(relx=0.5, rely=0.31, relwidth=0.1, relheight=0.05)

        # Bloco 5: "Em dias com ventos?" (Pergunta complementar)
        self.label_quest5 = ctk.CTkLabel(self.frame_right, text="Em dias com ventos?")
        self.label_quest5.place(relx=0.1, rely=0.38, relwidth=0.3, relheight=0.05)

        # Opções de números para a pergunta complementar 4 (1 a 4)
        self.entry_quest5 = ctk.CTkOptionMenu(self.frame_right, values=self.opcoes_quest1)
        self.entry_quest5.place(relx=0.5, rely=0.38, relwidth=0.1, relheight=0.05)

