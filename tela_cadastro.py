import re

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


PADRAO_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


class TelaCadastro(ctk.CTkFrame):
    def __init__(self, parent, trocar_tela, cadastrar_usuario, **kwargs):
        super().__init__(parent, **kwargs)

        self.trocar_tela = trocar_tela
        self.cadastrar_usuario = cadastrar_usuario

        self.label_titulo = ctk.CTkLabel(
            self,
            text="Criar conta",
            font=("High Tower Text", 18, "bold"),
        )
        self.label_titulo.pack(pady=(20, 14))

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.entry_nome.pack(pady=6, padx=20, fill="x")

        self.entry_email = ctk.CTkEntry(self, placeholder_text="E-mail")
        self.entry_email.pack(pady=6, padx=20, fill="x")

        self.entry_senha = ctk.CTkEntry(
            self,
            placeholder_text="Senha",
            show="*",
        )
        self.entry_senha.pack(pady=6, padx=20, fill="x")

        self.entry_confirmar_senha = ctk.CTkEntry(
            self,
            placeholder_text="Confirmar senha",
            show="*",
        )
        self.entry_confirmar_senha.pack(pady=6, padx=20, fill="x")
        self.entry_confirmar_senha.bind(
            "<Return>", lambda _event: self.cadastrar()
        )

        self.btn_enviar = ctk.CTkButton(
            self,
            text="Cadastrar",
            command=self.cadastrar,
        )
        self.btn_enviar.pack(pady=(12, 6))

        self.btn_visualizar = ctk.CTkButton(
            self,
            text="Mostrar senhas",
            command=self.alternar_visibilidade_senhas,
        )
        self.btn_visualizar.pack(pady=6)

        self.btn_voltar = ctk.CTkButton(
            self,
            text="Voltar ao login",
            command=lambda: self.trocar_tela("login"),
        )
        self.btn_voltar.pack(pady=6)

    def cadastrar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        erro = self.validar_campos(nome, email, senha, confirmar_senha)
        if erro:
            CTkMessagebox(
                title="Cadastro inválido",
                message=erro,
                icon="warning",
            )
            return

        sucesso, mensagem = self.cadastrar_usuario(nome, email, senha)
        CTkMessagebox(
            title="Cadastro confirmado" if sucesso else "Erro ao cadastrar",
            message=mensagem,
            icon="check" if sucesso else "cancel",
        )

        if sucesso:
            self.trocar_tela("login")

    @staticmethod
    def validar_campos(nome, email, senha, confirmar_senha):
        if not all((nome, email, senha, confirmar_senha)):
            return "Preencha todos os campos."
        if not PADRAO_EMAIL.match(email):
            return "Informe um endereço de e-mail válido."
        if len(senha) < 6:
            return "A senha deve possuir pelo menos 6 caracteres."
        if senha != confirmar_senha:
            return "As senhas não coincidem."
        return None

    def alternar_visibilidade_senhas(self):
        senhas_visiveis = self.entry_senha.cget("show") == ""
        novo_valor = "*" if senhas_visiveis else ""

        self.entry_senha.configure(show=novo_valor)
        self.entry_confirmar_senha.configure(show=novo_valor)
        self.btn_visualizar.configure(
            text="Mostrar senhas" if senhas_visiveis else "Ocultar senhas"
        )
