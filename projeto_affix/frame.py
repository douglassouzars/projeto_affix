import customtkinter as ctk
import json
from PIL import Image
from validate_docbr import CPF
import quest1
from dados import salvar_dados, carregar_dados

class Frame_esquerdo(ctk.CTkFrame):
    def __init__(self, master, image_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.width = 400
        self.height = 600

        self.frame_left = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color="white")
        self.frame_left.grid(row=0, column=0, sticky="nsew")

        image = Image.open(image_path).resize((self.width, self.height))
        self.image = ctk.CTkImage(light_image=image, dark_image=image, size=(self.width, self.height))

        self.image_label = ctk.CTkLabel(self.frame_left, image=self.image, text="")
        self.image_label.pack(expand=True)

class Frame_direito(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.width = 500
        self.height = 600

        self.frame_right = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color="grey")
        self.frame_right.grid(row=0, column=1, sticky="nsew")

        self.titulo = ctk.CTkLabel(self.frame_right, text="Cadastro", font=("Arial", 24, "bold"))
        self.titulo.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.07)

        # Campos de entrada
        self.entry_nome = self.criar_campo("Nome Completo:", 0.2, "Digite seu nome")
        self.entry_cpf = self.criar_campo("CPF:", 0.37, "Digite seu CPF", validar=self.validar_cpf_input)
        self.entry_email = self.criar_campo("Email:", 0.54, "Digite seu email")

        # Botão "Próximo"
        self.button_proximo = ctk.CTkButton(self.frame_right, text="Próximo", text_color='white', width=300, command=self.proximo)
        self.button_proximo.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.07)

        # Mensagens de erro
        self.mensagem_erro_cpf = ctk.CTkLabel(self.frame_right, text="", text_color="red", font=("Arial", 12))
        self.mensagem_erro_cpf.place(relx=0.1, rely=0.82, relwidth=0.8, relheight=0.05)

        self.mensagem_erro_email = ctk.CTkLabel(self.frame_right, text="", text_color="red", font=("Arial", 12))
        self.mensagem_erro_email.place(relx=0.1, rely=0.88, relwidth=0.8, relheight=0.05)

    def criar_campo(self, label_text, rel_y, placeholder, validar=None):
        """Função auxiliar para criar campos de entrada com rótulo."""
        label = ctk.CTkLabel(self.frame_right, text=label_text)
        label.place(relx=0.1, rely=rel_y, relwidth=0.8, relheight=0.05)

        if validar:
            vcmd = self.register(validar)
            entry = ctk.CTkEntry(self.frame_right, placeholder_text=placeholder, validate="key", validatecommand=(vcmd, '%P'))
        else:
            entry = ctk.CTkEntry(self.frame_right, placeholder_text=placeholder)

        entry.place(relx=0.1, rely=rel_y + 0.07, relwidth=0.8, relheight=0.07)
        return entry

    def validar_cpf_input(self, P):
        """Permite entrada de apenas números e no máximo 11 dígitos."""
        return P.isdigit() and len(P) <= 11 or P == ""

    def validar_cpf(self, cpf):
        """Valida o CPF usando a biblioteca validate-docbr."""
        return CPF().validate(cpf)

    def validar_email(self, email):
        """Valida o e-mail verificando a presença de '@' e '.'."""
        return "@" in email and "." in email

    def salvar_dados(self, nome, cpf, email):
        """Salva os dados em um arquivo JSON."""
        nome_arquivo = f"{nome.replace(' ', '_')}_dados.json"
        dados = {"nome": nome, "cpf": cpf, "email": email}

        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4)
            print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def proximo(self):
        """Valida os dados e avança para a próxima etapa."""
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        cpf_valido = self.validar_cpf(cpf)
        email_valido = self.validar_email(email)

        if not cpf_valido:
            self.mensagem_erro_cpf.configure(text="CPF inválido!")
            self.entry_cpf.focus()
        else:
            self.mensagem_erro_cpf.configure(text="")

        if not email_valido:
            self.mensagem_erro_email.configure(text="E-mail inválido! Deve conter '@' e '.'")
            self.entry_email.focus()
        else:
            self.mensagem_erro_email.configure(text="")

        if cpf_valido and email_valido:
            print(f"Nome: {nome}, CPF: {cpf}, Email: {email}")
           # self.salvar_dados(nome, cpf, email)
            self.mudar_frame_direito(nome, cpf, email)

    def mudar_frame_direito(self, nome, cpf, email):
        """Troca o conteúdo do frame direito pelo formulário do quest1."""
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        def voltar_callback():
            print("Voltando para a tela inicial...")
            self.voltar()

        def proximo_callback():
            print("Avançando para as próximas questões...")

        quest_frame = quest1.QuestFrame(self.frame_right, voltar_callback=voltar_callback, proximo_callback=proximo_callback)
        quest_frame.pack(fill="both", expand=True)

    def voltar(self):
        """Restaura o formulário inicial."""
        for widget in self.frame_right.winfo_children():
            widget.destroy()

        self.titulo = ctk.CTkLabel(self.frame_right, text="Cadastro", font=("Arial", 24, "bold"))
        self.titulo.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.07)

        self.entry_nome = self.criar_campo("Nome Completo:", 0.2, "Digite seu nome")
        self.entry_cpf = self.criar_campo("CPF:", 0.37, "Digite seu CPF", validar=self.validar_cpf_input)
        self.entry_email = self.criar_campo("Email:", 0.54, "Digite seu email")

        self.button_proximo = ctk.CTkButton(self.frame_right, text="Próximo", text_color='white', width=300, command=self.proximo)
        self.button_proximo.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.07)
