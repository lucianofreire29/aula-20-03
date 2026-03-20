import customtkinter as ctk 
from CTkMessagebox import CTkMessagebox as mg


class TelaCadastro(ctk.CTkFrame):
    def __init__(self, parent, trocar_tela, **kwargs):
        super().__init__(parent, **kwargs)


        self.trocar_tela = trocar_tela

        # titulo
        self.label_titulo = ctk.CTkLabel(
                                    self,
                                    text="criar conta",
                                    font=("High Tower Text", 18, "bold")
                                        )
        self.label_titulo.pack(pady=10)

        # campos
        self.entry_nome = ctk.CTkEntry(self,
                                    placeholder_text="Nome")
        self.entry_nome.pack(pady=6, padx=10, fill="x")

        self.entry_Email = ctk.CTkEntry(self,
                                        placeholder_text="Email")
        self.entry_Email.pack(pady=6, padx=10, fill="x")

        self.entry_senha = ctk.CTkEntry(self,
                                        placeholder_text="senha",
                                        show="*")
        self.entry_senha.pack(pady=6, padx=10, fill="x")

        self.entry_conf_senha = ctk.CTkEntry(self,
                                            placeholder_text="confirmar senha",
                                            show="*")
        self.entry_conf_senha.pack(pady=6, padx=10, fill="x")

        # botões
        self.btn_enviar = ctk.CTkButton(self,
                                        text="Enviar",
                                        command=self.cadastrar)
        self.btn_enviar.pack(pady=6)

        self.btn_visualizar = ctk.CTkButton(self,
                                            text="visualizar senha",
                                            command=self.visualizar_senhas)
        self.btn_visualizar.pack(pady=6)

        self.btn_voltar = ctk.CTkButton(
            self,
            text="Voltar",
            command=lambda: self.trocar_tela("login")
        )
        self.btn_voltar.pack(pady=6)





    def cadastrar(self):
        senha = self.entry_senha.get()
        conf_senha = self.entry_conf_senha.get()

        if senha == conf_senha and senha != "":
            mg(
                title="Cadastro confirmado",
                message=f"Usuário {self.entry_nome.get()} foi cadastrado com sucesso!",
                icon="check"
            )
        else:
            mg(
                title="Erro ao cadastrar!",
                message="Senhas inválidas!",
                icon="cancel"
            )

    def visualizar_senhas(self):
        if self.entry_senha.cget("show") == "*":
            self.entry_senha.configure(show="")
            self.entry_conf_senha.configure(show="")
            self.btn_visualizar.configure(text="ocultar senhas")
        else:
            self.entry_senha.configure(show="*")
            self.entry_conf_senha.configure(show="*")
            self.btn_visualizar.configure(text="mostrar senhas")


