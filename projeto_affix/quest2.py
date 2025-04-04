import customtkinter as ctk
import subprocess

class QuestFrame(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, proximo_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.voltar_callback = voltar_callback
        self.proximo_callback = proximo_callback

        self.width = 500
        self.height = 600
        self.configure(width=self.width, height=self.height, fg_color="grey")

        self.pack_propagate(False)  # Impede redimensionamento automático

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

        self.respostas_vars = {}

        # Frame para a rolagem
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=475, height=450)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        for i, (pergunta, opcoes) in enumerate(self.perguntas):
            lbl_pergunta = ctk.CTkLabel(self.scroll_frame, text=pergunta, font=("Arial", 14, "bold"), wraplength=450)
            lbl_pergunta.pack(anchor="w", pady=5)

            self.respostas_vars[i] = {}

            for j, opcao in enumerate(opcoes):
                frame_opcao = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
                frame_opcao.pack(fill="x")

                lbl_opcao = ctk.CTkLabel(frame_opcao, text=opcao, wraplength=400, anchor="w", justify="left")
                lbl_opcao.pack(side="left", padx=5)

                entry_var = ctk.StringVar()
                entry_opcao = ctk.CTkOptionMenu(frame_opcao, values=["1", "2", "3", "4"], variable=entry_var)
                entry_opcao.pack(side="right", padx=5)

                self.respostas_vars[i][opcao] = entry_var

        self.lbl_erro = ctk.CTkLabel(self, text="", font=("Arial", 12, "bold"), text_color="red")
        self.lbl_erro.pack(pady=5)

        # Criando frame para botões e fixando na parte inferior
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(fill="x", side="bottom")  # Ocupar toda a largura

        # Botão Voltar
        self.btn_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar_callback, fg_color="red")
        self.btn_voltar.pack(side="left", fill="x", expand=True, padx=10, pady=5)

        # Botão Próximo
        self.btn_proximo = ctk.CTkButton(self.frame_botoes, text="Próximo", command=self.processar_respostas)
        self.btn_proximo.pack(side="right", fill="x", expand=True, padx=10, pady=5)


    def processar_respostas(self):
        for i, opcoes in self.respostas_vars.items():
            valores = [var.get() for var in opcoes.values()]
            if len(valores) != len(set(valores)):
                self.lbl_erro.configure(text=f"Erro na Pergunta {i+1}: Os números não podem se repetir!")
                return

        self.lbl_erro.configure(text="")
        self.master.destroy()
        subprocess.run(["python", "quest3.py"])
