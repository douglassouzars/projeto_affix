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

        self.titulo = ctk.CTkLabel(self, text="Questionário DISC - Parte 2", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=10)
        print("ACESSOU QUEST2")

        # Definição das perguntas e respostas
        self.perguntas = [
            ("Como você normalmente reage diante de conflitos ou desentendimentos?",
                ["A. Sinto receio e posso ficar magoado com facilidade.",
                 "B. Resolvo rapidamente o problema",
                 "C. Às vezes, posso agir de forma assertiva para resolver a situação.",
                 "D. Prefiro me manter em silêncio e me afastar da situação."]),
            
            ("Qual é a sua atitude predominante em relação às compras e gastos?",
                ["A. Tenho atração por ofertas e descontos e frequentemente compro.",
                 "B. Sinto prazer ao fazer compras, muitas vezes comprando coisas não essenciais.",
                 "C. Sou decidido e só gasto dinheiro quando encontro exatamente o que desejo.	",
                 "D. Tenho dificuldade em tomar decisões e escolher produtos."]),
            
            ("Como você geralmente interage e se relaciona com os outros?",
                ["A. Prefiro estar com pessoas que sejam fáceis de conviver e evito conflitos.	",
                 "B. Tendo a animar e trazer alegria a pessoas que estejam tristes.",
                 "C. Gosto de realizar várias tarefas simultaneamente.	",
                 "D. Prefiro interagir com pessoas resolvendo problemas que requerem raciocionio e encontrando soluções."])
        ]

        self.respostas_vars = {}

        # Criando um frame com rolagem
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=470, height=420)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        for i, (pergunta, opcoes) in enumerate(self.perguntas):
            # Definir a largura do texto para que quebre a linha automaticamente
            lbl_pergunta = ctk.CTkLabel(self.scroll_frame, text=pergunta, font=("Arial", 14, "bold"),
                                        wraplength=450, anchor="w", justify="left")
            lbl_pergunta.pack(anchor="w", pady=5)

            self.respostas_vars[i] = {}

            for opcao in opcoes:
                frame_opcao = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
                frame_opcao.pack(fill="x", padx=5, pady=2)

                lbl_opcao = ctk.CTkLabel(frame_opcao, text=opcao, wraplength=400, anchor="w", justify="left")
                lbl_opcao.pack(side="left", padx=5)

                entry_var = ctk.StringVar()
                entry_opcao = ctk.CTkOptionMenu(frame_opcao, values=["1", "2", "3", "4"], variable=entry_var)
                entry_opcao.pack(side="right", padx=5)

                self.respostas_vars[i][opcao] = entry_var

        # Rótulo para mensagens de erro
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
        """Captura as respostas do usuário e exibe erro se houver números repetidos"""
        for i, opcoes in self.respostas_vars.items():
            valores = [var.get() for var in opcoes.values()]
            if len(valores) != len(set(valores)):  # Verifica se há valores repetidos
                self.lbl_erro.configure(text=f"Erro na Pergunta {i+1}: Os números não podem se repetir!")
                return

        # Se não houver erro, limpa a mensagem e chama o próximo questionário
        self.lbl_erro.configure(text="")
        self.master.destroy()
        subprocess.run(["python", "quest4.py"])
