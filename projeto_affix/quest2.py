import customtkinter as ctk

class Quest2Frame(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.voltar_callback = voltar_callback

        self.width = 500
        self.height = 600
        self.configure(width=self.width, height=self.height, fg_color="grey")

        # Frame esquerdo para manter o layout
        self.frame_esquerdo = ctk.CTkFrame(self, width=150, height=self.height, fg_color="darkgrey")
        self.frame_esquerdo.pack(side="left", fill="y")

        self.titulo = ctk.CTkLabel(self, text="Questionário DISC - Parte 2", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=10)

        self.perguntas = [
            ("No ambiente de trabalho, o que você valoriza mais?",
                ["A. Uma rotina previsível e estruturada.",
                 "B. A aprovação e o reconhecimento dos outros.",
                 "C. Ter controle sobre as situações e decisões.",
                 "D. Regras claras e bem definidas para orientar ações."]),
            
            ("O que mais desperta a sua motivação e interesse na vida?",
                ["A. Enfrentar desafios, explorar novas ideias e criar coisas novas.",
                 "B. Experimentar surpresas agradáveis, se divertir com amigos e ter momentos inesperados.",
                 "C. Receber carinho e aceitação de pessoas ao seu redor.",
                 "D. Buscar constantemente aprendizado, sabedoria e adquirir novos conhecimentos."]),
            
            ("Qual das seguintes áreas você sente que é mais o seu ponto forte?",
                ["A. Tomar decisões rapidamente e agir com firmeza.",
                 "B. Lidar com relações públicas e interações sociais.",
                 "C. Ter a habilidade de se adaptar bem em equipes diversas.",
                 "D. Priorizar a qualidade e a pontualidade para se sentir seguro."])
        ]

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=325, height=450)
        self.scroll_frame.pack(side="right", pady=10, padx=10, fill="both", expand=True)

        for pergunta, opcoes in self.perguntas:
            lbl_pergunta = ctk.CTkLabel(self.scroll_frame, text=pergunta, font=("Arial", 14, "bold"))
            lbl_pergunta.pack(anchor="w", pady=5)

            for opcao in opcoes:
                frame_opcao = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
                frame_opcao.pack(fill="x")

                lbl_opcao = ctk.CTkLabel(frame_opcao, text=opcao)
                lbl_opcao.pack(side="left", padx=5)

        # Criando frame para os botões na parte inferior
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(fill="x", pady=10)

        # Botão Voltar
        self.btn_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar_callback, fg_color="red")
        self.btn_voltar.pack(side="left", padx=10, expand=True)

        # Botão Finalizar
        self.btn_finalizar = ctk.CTkButton(self.frame_botoes, text="Finalizar", command=self.finalizar)
        self.btn_finalizar.pack(side="right", padx=10, expand=True)

    def finalizar(self):
        self.master.destroy()

# Função para voltar para quest.py
def voltar_para_quest():
    import subprocess
    root.destroy()
    subprocess.run(["python", "quest.py"])

# Criando a janela principal
root = ctk.CTk()
root.geometry("500x600")
app = Quest2Frame(root, voltar_callback=voltar_para_quest)
app.pack(fill="both", expand=True)
root.mainloop()
