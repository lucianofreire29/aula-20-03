import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as mg
from tela_cadastro import TelaCadastro

class TelaLogin(ctk.CTkFrame):
    def __init__(self, parent, trocar_tela, **kwargs):
        super().__init__(parent, **kwargs)

        self.trocar_tela = trocar_tela
    # aidiconar os componentes

        # titulo
        self.label_titulo = ctk.CTkLabel(
                                    self,
                                    text="Login",
                                    font=("High Tower Text", 18, "bold")
                                        )
        self.label_titulo.pack(pady=10)

        self.entry_Email = ctk.CTkEntry(self,height=40
                                        ,placeholder_text="Email")
        self.entry_Email.pack(pady=6, padx=10, fill="x")
        


        self.entry_senha = ctk.CTkEntry(self,
                                        height=40,
                                        placeholder_text="senha",
                                        show="*")
        self.entry_senha.pack(pady=6, padx=10, fill="x")

        self.check_box = ctk.CTkCheckBox(self,text="lembrar-me")
        self.check_box.pack(pady=6,padx=10,fill="x")

        self.btn_enviar = ctk.CTkButton(self,
                                        text="Login",
                                        )
        self.btn_enviar.pack(pady=6)

        self.btn_visualizar = ctk.CTkButton(self,
                                            text="visualizar senha",
                                            command=self.visualizar_senhas)
        self.btn_visualizar.pack(pady=6)



        self.btn_cadastrar = ctk.CTkButton(
            self,
            text="Cadastrar",
            command=lambda: self.trocar_tela("cadastro")
        )
        self.btn_cadastrar.pack(pady=6)

    def visualizar_senhas(self):
        if self.entry_senha.cget("show") == "*":
            self.entry_senha.configure(show="")

            self.btn_visualizar.configure(text="ocultar senhas")
        else:
            self.entry_senha.configure(show="*")

            self.btn_visualizar.configure(text="mostrar senhas")








# aidiconar os metodos