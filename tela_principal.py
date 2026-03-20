import customtkinter as ctk
from tela_login import TelaLogin
from tela_cadastro import TelaCadastro


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Seja Bem Vindo ao SmartSystem")
        self.geometry("420x500")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")


        self.current_frame = TelaLogin(self, self.trocar_tela)
        self.current_frame.pack(pady=10, padx=10,fill="both",expand=True)




    def trocar_tela(self, nome_tela):
            if self.current_frame is not None:
                self.current_frame.destroy()

            if nome_tela == "login":
                self.current_frame = TelaLogin(self, self.trocar_tela)
            elif nome_tela == "cadastro":
                self.current_frame = TelaCadastro(self, self.trocar_tela)

            self.current_frame.pack(fill="both", expand=True, padx=10, pady=10)




















    #     self.current_frame = TelaLogin(parent=self, form=lambda: self.trocar_tela("cadastro"))
    #     self.current_frame.pack(pady=10, padx=10,fill="both",expand=True)


    # def trocar_tela(self, nome_tela: str):
    #     if nome_tela == "cadastro":
    #         ...
    #     elif nome_tela == "login":