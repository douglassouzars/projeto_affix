import customtkinter as ctk
from PIL import Image, ImageTk
from validate_docbr import CPF
import quest 

class Frame_esquerdo(ctk.CTkFrame):
    def __init__(self, master, image_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Definir a largura e altura do frame
        self.width = 400
        self.height = 600
        
        # Criar o frame esquerdo com fundo branco
        self.frame_left = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color="white")
        self.frame_left.grid(row=0, column=0, sticky="nsew")  # Usando grid para controlar o layout

        # Carregar a imagem usando Pillow
        image = Image.open(image_path)  # Carregar a imagem
        image = image.resize((self.width, self.height))  # Redimensionar a imagem para o tamanho do frame
        
        # Converter a imagem para um formato que CustomTkinter entenda
        self.image = ctk.CTkImage(light_image=image, dark_image=image, size=(self.width, self.height))

        # Exibir a imagem no lado esquerdo, sem texto
        self.image_label = ctk.CTkLabel(self.frame_left, image=self.image, text="")  # Definindo text="" para não aparecer texto
        self.image_label.pack(expand=True)

class Frame_direito(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Definir a largura e altura do frame
        self.width = 500
        self.height = 600
        
        # Criar o frame direito com fundo cinza
        self.frame_right = ctk.CTkFrame(self, width=self.width, height=self.height, fg_color="grey")
        self.frame_right.grid(row=0, column=1, sticky="nsew")  # Usando grid para controlar o layout

        # Adicionar título ao Frame direito
        self.titulo = ctk.CTkLabel(self.frame_right, text="Cadastro", font=("Arial", 24, "bold"))
        self.titulo.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.07)  # Título no topo

        # Campo Nome
        self.label_nome = ctk.CTkLabel(self.frame_right, text="Nome Completo:")
        self.label_nome.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)  # Rótulo Nome
        self.entry_nome = ctk.CTkEntry(self.frame_right, placeholder_text="Digite seu nome")
        self.entry_nome.place(relx=0.1, rely=0.27, relwidth=0.8, relheight=0.07)  # Campo de entrada para nome

        # Campo CPF (apenas números e válido)
        self.label_cpf = ctk.CTkLabel(self.frame_right, text="CPF:")
        self.label_cpf.place(relx=0.1, rely=0.37, relwidth=0.8, relheight=0.05)  # Rótulo CPF

        # Função para validar o CPF e garantir que tenha até 11 dígitos
        def validar_cpf_input(P):
            # Se o texto for vazio, permite que o usuário continue digitando
            if len(P) <= 11 and P.isdigit():
                return True
            elif len(P) == 0:  # Permite apagar todo o conteúdo
                return True
            return False

        # Registra a função de validação do CPF
        vcmd = self.register(validar_cpf_input)
        self.entry_cpf = ctk.CTkEntry(self.frame_right, placeholder_text="Digite seu CPF", validate="key", validatecommand=(vcmd, '%P'))
        self.entry_cpf.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.07)  # Campo de entrada para CPF

        # Campo Email
        self.label_email = ctk.CTkLabel(self.frame_right, text="Email:")
        self.label_email.place(relx=0.1, rely=0.54, relwidth=0.8, relheight=0.05)  # Rótulo Email
        self.entry_email = ctk.CTkEntry(self.frame_right, placeholder_text="Digite seu email")
        self.entry_email.place(relx=0.1, rely=0.61, relwidth=0.8, relheight=0.07)  # Campo de entrada para email

        # Botão "Próximo"
        self.button_proximo = ctk.CTkButton(self.frame_right, text_color='white', text="Próximo", width=300, command=self.proximo)
        self.button_proximo.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.07)  # Botão no final

        # Label para mostrar a mensagem de erro de CPF
        self.mensagem_erro_cpf = ctk.CTkLabel(self.frame_right, text="", text_color="red", font=("Arial", 12))
        self.mensagem_erro_cpf.place(relx=0.1, rely=0.82, relwidth=0.8, relheight=0.05)

        # Label para mostrar a mensagem de erro de E-mail
        self.mensagem_erro_email = ctk.CTkLabel(self.frame_right, text="", text_color="red", font=("Arial", 12))
        self.mensagem_erro_email.place(relx=0.1, rely=0.88, relwidth=0.8, relheight=0.05)

    def validar_cpf(self, cpf):
        """Função de validação para garantir que o CPF é válido."""
        cpf_validator = CPF()
        return cpf_validator.validate(cpf)

    def validar_email(self, email):
        """Função de validação para garantir que o E-mail é válido."""
        return "@" in email and "." in email

    def proximo(self):
        """Aqui você pode adicionar a lógica para o que acontece quando o botão 'Próximo' é clicado."""
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        # Validação do CPF
        if not self.validar_cpf(cpf):
            self.mensagem_erro_cpf.configure(text="CPF inválido!")  # Exibe a mensagem de erro
            self.entry_cpf.focus()  # Foca no campo CPF para facilitar a correção do erro
        else:
            self.mensagem_erro_cpf.configure(text="")  # Limpa a mensagem de erro

        # Validação do E-mail
        if not self.validar_email(email):
            self.mensagem_erro_email.configure(text="E-mail inválido! O e-mail deve conter '@'.")  # Exibe a mensagem de erro
            self.entry_email.focus()  # Foca no campo de email para facilitar a correção do erro
        else:
            self.mensagem_erro_email.configure(text="")  # Limpa a mensagem de erro

        if self.validar_cpf(cpf) and self.validar_email(email):
            print(f"Nome: {nome}, CPF: {cpf}, Email: {email}")
            # Aqui você pode adicionar a lógica de navegação ou validação dos dados
            
            # Mudar o conteúdo do Frame_direito para o formulário do quest.py
            self.mudar_frame_direito(nome, cpf, email)

    def mudar_frame_direito(self, nome, cpf, email):
        """Altera o conteúdo do Frame_direito para o próximo formulário (quest.py)."""
        for widget in self.frame_right.winfo_children():
            widget.destroy()  # Remove todos os widgets do Frame_direito
        
        # Agora carregue o conteúdo de quest.py dentro do Frame_direito
        quest_frame = quest.QuestFrame(self.frame_right, nome, cpf, email)  # Passa os dados para o QuestFrame
        quest_frame.pack(fill="both", expand=True)