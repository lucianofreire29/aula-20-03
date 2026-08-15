import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class TelaLogin(ctk.CTkFrame):
    def __init__(self, parent, trocar_tela, autenticar_usuario, **kwargs):
        super().__init__(parent, **kwargs)

        self.trocar_tela = trocar_tela
        self.autenticar_usuario = autenticar_usuario

        self.label_titulo = ctk.CTkLabel(
            self,
            text="Login",
            font=("High Tower Text", 18, "bold"),
        )
        self.label_titulo.pack(pady=(30, 18))

        self.entry_email = ctk.CTkEntry(
            self,
            height=40,
            placeholder_text="E-mail",
        )
        self.entry_email.pack(pady=6, padx=20, fill="x")

        self.entry_senha = ctk.CTkEntry(
            self,
            height=40,
            placeholder_text="Senha",
            show="*",
        )
        self.entry_senha.pack(pady=6, padx=20, fill="x")
        self.entry_senha.bind("<Return>", lambda _event: self.entrar())

        self.checkbox_lembrar = ctk.CTkCheckBox(self, text="Lembrar-me")
        self.checkbox_lembrar.pack(pady=8, padx=20, anchor="w")

        self.btn_entrar = ctk.CTkButton(
            self,
            text="Entrar",
            command=self.entrar,
        )
        self.btn_entrar.pack(pady=(12, 6))

        self.btn_visualizar = ctk.CTkButton(
            self,
            text="Mostrar senha",
            command=self.alternar_visibilidade_senha,
        )
        self.btn_visualizar.pack(pady=6)

        self.btn_cadastrar = ctk.CTkButton(
            self,
            text="Criar conta",
            command=lambda: self.trocar_tela("cadastro"),
        )
        self.btn_cadastrar.pack(pady=6)

    def entrar(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get()

        if not email or not senha:
            CTkMessagebox(
                title="Campos obrigatórios",
                message="Informe o e-mail e a senha.",
                icon="warning",
            )
            return

        sucesso, mensagem = self.autenticar_usuario(email, senha)
        CTkMessagebox(
            title="Login realizado" if sucesso else "Falha no login",
            message=mensagem,
            icon="check" if sucesso else "cancel",
        )

        if sucesso:
            self.entry_senha.delete(0, "end")

    def alternar_visibilidade_senha(self):
        senha_visivel = self.entry_senha.cget("show") == ""
        self.entry_senha.configure(show="*" if senha_visivel else "")
        self.btn_visualizar.configure(
            text="Mostrar senha" if senha_visivel else "Ocultar senha"
        )
