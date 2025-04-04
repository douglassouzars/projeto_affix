import customtkinter as ctk
import subprocess

class QuestFrame(ctk.CTkFrame):
    def __init__(self, parent, nome, cpf, email, perguntas, voltar_callback, proximo_callback):
        super().__init__(parent)
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.voltar_callback = voltar_callback
        self.proximo_callback = proximo_callback

        self.width = 500
        self.height = 600
        self.configure(width=self.width, height=self.height, fg_color="grey")

        self.titulo = ctk.CTkLabel(self, text="Questionário DISC", font=("Arial", 24, "bold"))
        self.titulo.pack(pady=10)

        self.perguntas = perguntas  # Recebe perguntas importadas
        self.respostas_vars = {}  # Armazena as variáveis de resposta

        # Criando perguntas dinamicamente
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=475, height=450)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        for i, (pergunta, opcoes) in enumerate(self.perguntas):
            lbl_pergunta = ctk.CTkLabel(self.scroll_frame, text=pergunta, font=("Arial", 14, "bold"))
            lbl_pergunta.pack(anchor="w", pady=5)

            self.respostas_vars[i] = {}

            for j, opcao in enumerate(opcoes):
                frame_opcao = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
                frame_opcao.pack(fill="x")

                lbl_opcao = ctk.CTkLabel(frame_opcao, text=opcao)
                lbl_opcao.pack(side="left", padx=5)

                entry_var = ctk.StringVar()
                entry_opcao = ctk.CTkOptionMenu(frame_opcao, values=["1", "2", "3", "4"], variable=entry_var)
                entry_opcao.pack(side="right", padx=5)

                self.respostas_vars[i][opcao] = entry_var

        # Rótulo para mensagens de erro
        self.lbl_erro = ctk.CTkLabel(self, text="", font=("Arial", 12, "bold"), text_color="red")
        self.lbl_erro.pack(pady=5)

        # Criando frame para os botões na parte inferior
        self.frame_botoes = ctk.CTkFrame(self)
        self.frame_botoes.pack(fill="x", pady=10)

        # Botão Voltar
        self.btn_voltar = ctk.CTkButton(self.frame_botoes, text="Voltar", command=self.voltar_callback, fg_color="red")
        self.btn_voltar.pack(side="left", padx=10, expand=True)

        # Botão Próximas Questões
        self.btn_proximo = ctk.CTkButton(self.frame_botoes, text="Próximas Questões", command=self.processar_respostas)
        self.btn_proximo.pack(side="right", padx=10, expand=True)

    def processar_respostas(self):
        """Captura as respostas do usuário e exibe erro em vermelho se houver números repetidos"""
        for i, opcoes in self.respostas_vars.items():
            valores = [var.get() for var in opcoes.values()]
            if len(valores) != len(set(valores)):  # Verifica se há valores repetidos
                self.lbl_erro.configure(text=f"Erro na Pergunta {i+1}: Os números não podem se repetir!")
                return

        # Se não houver erro, limpa a mensagem e chama o próximo questionário
        self.lbl_erro.configure(text="")
        self.master.destroy()  # Fecha a janela atual
        if self.proximo_arquivo:
            subprocess.run(["python", self.proximo_arquivo])  # Executa o próximo questionário
