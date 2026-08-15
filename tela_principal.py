import customtkinter as ctk

from tela_cadastro import TelaCadastro
from tela_login import TelaLogin


class App(ctk.CTk):
    """Janela principal e estado da aplicação."""

    def __init__(self):
        super().__init__()

        self.title("SmartSystem")
        self.geometry("420x500")
        self.minsize(380, 460)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

        self.usuarios = {}
        self.current_frame = None
        self.trocar_tela("login")

    def cadastrar_usuario(self, nome, email, senha):
        """Cadastra um usuário apenas durante a execução do programa."""
        email_normalizado = email.strip().lower()

        if email_normalizado in self.usuarios:
            return False, "Este e-mail já está cadastrado."

        self.usuarios[email_normalizado] = {
            "nome": nome.strip(),
            "senha": senha,
        }
        return True, "Cadastro realizado com sucesso!"

    def autenticar_usuario(self, email, senha):
        """Valida as credenciais de um usuário cadastrado na sessão atual."""
        usuario = self.usuarios.get(email.strip().lower())

        if usuario is None or usuario["senha"] != senha:
            return False, "E-mail ou senha incorretos."

        return True, f"Bem-vindo, {usuario['nome']}!"

    def trocar_tela(self, nome_tela):
        if self.current_frame is not None:
            self.current_frame.destroy()

        if nome_tela == "login":
            self.current_frame = TelaLogin(
                self,
                trocar_tela=self.trocar_tela,
                autenticar_usuario=self.autenticar_usuario,
            )
        elif nome_tela == "cadastro":
            self.current_frame = TelaCadastro(
                self,
                trocar_tela=self.trocar_tela,
                cadastrar_usuario=self.cadastrar_usuario,
            )
        else:
            raise ValueError(f"Tela desconhecida: {nome_tela}")

        self.current_frame.pack(fill="both", expand=True, padx=10, pady=10)
